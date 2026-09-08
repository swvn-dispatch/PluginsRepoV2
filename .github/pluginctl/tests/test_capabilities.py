from pluginctl import capabilities


def test_future_manifest_versions_use_latest_enforcing_policy():
    assert capabilities.manifest_version_enforces_sandbox(99)
    assert capabilities.manifest_version_parses_capabilities(99)


def test_legacy_and_transition_versions_remain_non_enforcing():
    assert not capabilities.manifest_version_enforces_sandbox(0)
    assert not capabilities.manifest_version_enforces_sandbox(1)
    assert capabilities.manifest_version_enforces_sandbox(2)
    assert capabilities.first_enforcing_manifest_version() == 2


def test_declared_capabilities_preserve_unknown_future_values():
    manifest = {"manifest_version": 99, "capabilities": ["subprocess", "future_capability"]}
    assert capabilities.declared_capabilities(manifest) == {"subprocess", "future_capability"}


def test_legacy_manifest_does_not_parse_capabilities():
    assert capabilities.declared_capabilities({"capabilities": ["subprocess"]}) == set()
