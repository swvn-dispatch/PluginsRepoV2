"""Behavior added by upstream PR #127, reimplemented in the pluginctl publish path."""

import json

from pluginctl.publish import manifest as m
from pluginctl.publish import zips


# ---- immutable-tag release retry ----
def test_classify_release_error():
    assert zips.classify_release_error("a release with the same tag already exists") == "exists"
    assert zips.classify_release_error("tag is immutable and cannot be moved") == "immutable"
    assert zips.classify_release_error("Cannot create ref, already exists as immutable") == "exists"
    assert zips.classify_release_error("Cannot create ref refs/tags/x") == "immutable"
    assert zips.classify_release_error("network error 500") == "fatal"


def test_upload_retry_suffixes_on_immutable(monkeypatch):
    calls = []

    def fake_create(tag, repo, title, notes, asset):
        calls.append(tag)
        if tag == "demo-1.0.0":
            return 1, "tag is immutable"
        return 0, ""

    monkeypatch.setattr(zips.gh, "release_create_capture", fake_create)
    final_tag, skipped = zips._upload_with_retry("demo-1.0.0", "org/repo", "t", "n", "z.zip")
    assert final_tag == "demo-1.0.0-1"
    assert skipped is False
    assert calls == ["demo-1.0.0", "demo-1.0.0-1"]


def test_upload_skip_when_release_exists(monkeypatch):
    monkeypatch.setattr(zips.gh, "release_create_capture",
                        lambda *a: (1, "release already exists"))
    final_tag, skipped = zips._upload_with_retry("demo-1.0.0", "org/repo", "t", "n", "z.zip")
    assert final_tag == "demo-1.0.0" and skipped is True


def test_upload_fatal_returns_none(monkeypatch):
    monkeypatch.setattr(zips.gh, "release_create_capture", lambda *a: (1, "boom"))
    assert zips._upload_with_retry("demo-1.0.0", "org/repo", "t", "n", "z.zip") is None


# ---- icon sync ----
def test_sync_icon_prefers_png(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    pdir = tmp_path / "plugins" / "demo"
    pdir.mkdir(parents=True)
    (pdir / "logo.png").write_bytes(b"png")
    (pdir / "logo.svg").write_bytes(b"svg")
    (tmp_path / "metadata" / "demo").mkdir(parents=True)
    m._sync_icon(str(pdir) + "/", "demo")
    assert (tmp_path / "metadata" / "demo" / "logo.png").read_bytes() == b"png"
    assert not (tmp_path / "metadata" / "demo" / "logo.svg").exists()


def test_sync_icon_falls_back_to_webp(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    pdir = tmp_path / "plugins" / "demo"
    pdir.mkdir(parents=True)
    (pdir / "logo.webp").write_bytes(b"webp")
    (tmp_path / "metadata" / "demo").mkdir(parents=True)
    m._sync_icon(str(pdir) + "/", "demo")
    assert (tmp_path / "metadata" / "demo" / "logo.webp").read_bytes() == b"webp"


def test_sync_icon_no_logo_is_noop(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    pdir = tmp_path / "plugins" / "demo"
    pdir.mkdir(parents=True)
    (tmp_path / "metadata" / "demo").mkdir(parents=True)
    m._sync_icon(str(pdir) + "/", "demo")
    assert list((tmp_path / "metadata" / "demo").iterdir()) == []


# ---- canonical ZIP filename in version url (retry suffix in dir, not filename) ----
def test_version_entry_url_uses_canonical_filename():
    # generate() builds this url; assert the composition rule directly
    zip_version = "1.0.0-1"           # release tag carried a retry suffix
    canonical = m._canonical(zip_version)
    assert canonical == "1.0.0"
    url = f"demo-{zip_version}/demo-{canonical}.zip"
    assert url == "demo-1.0.0-1/demo-1.0.0.zip"
    entry = m.build_version_entry({"version": canonical}, url, 5, canonical)
    assert entry["url"] == "demo-1.0.0-1/demo-1.0.0.zip"
