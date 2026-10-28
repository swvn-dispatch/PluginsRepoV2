[Back to All Plugins](../../README.md)

# VOD Probe

**Version:** `1.3.4` | **Author:** oxios0x00 | **Last Updated:** Oct 24 2026, 07:02 UTC

Probes the real quality of each VOD relation (movies and every episode of every series version) with ffprobe in a background task and writes it into the relation's custom_properties, so every tool reading Dispatcharr's API can use it. Can also backfill missing tmdb_id/imdb_id from the provider's per-title detail endpoint, merging safely into an existing catalogue entry when one already has the id. Dry run by default.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://spdx.org/licenses/MIT.html) [![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/oxios0x00/dispatcharr-vod-probe)

## Downloads

### Latest Release

- **Download:** [`vod-probe-latest.zip`](https://github.com/swvn-dispatch/plugin-repo-dev/releases/download/vod-probe-1.3.4/vod-probe-1.3.4.zip)
- **Built:** Oct 28 2026, 13:36 UTC
- **Source Commit:** [`6aed020`](https://github.com/swvn-dispatch/plugin-repo-dev/commit/6aed02022cc080d7109f9519db52b6982313c0af)

**Checksums:**
```
MD5:    49cbe14431df756e75bfa8b984e01f29
SHA256: a89db1c6556167ab267a218a82aef56016df61babb37f67ffeaef4898cd7f3c2
```

### All Versions

| Version | Download | Built | Commit | MD5 | SHA256 |
|---------|----------|-------|--------|-----|--------|
| `1.3.4` | [Download](https://github.com/swvn-dispatch/plugin-repo-dev/releases/download/vod-probe-1.3.4/vod-probe-1.3.4.zip) | Oct 28 2026, 13:36 UTC | [`6aed020`](https://github.com/swvn-dispatch/plugin-repo-dev/commit/6aed02022cc080d7109f9519db52b6982313c0af) | 49cbe14431df756e75bfa8b984e01f29 | a89db1c6556167ab267a218a82aef56016df61babb37f67ffeaef4898cd7f3c2 |

---

**Source:** [Browse Plugin](https://github.com/swvn-dispatch/plugin-repo-dev/tree/main/plugins/vod-probe)

**Metadata:** [View full manifest](./manifest.json)
