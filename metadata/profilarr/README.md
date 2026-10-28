[Back to All Plugins](../../README.md)

# Profilarr

**Version:** `2.1.6` | **Author:** Tw1zT3d2four7 | **Last Updated:** Sep 24 2026, 04:31 UTC

Hybrid ffmpeg + cvlc stream profiles. ffmpeg fetches the provider stream directly with a custom user-agent and reconnect handling, and regenerates timestamps (+genpts+igndts+discardcorrupt); cvlc then buffers and delivers the already-clean stream, so downstream players don't freeze on a CDN-hiccup discontinuity.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://spdx.org/licenses/MIT.html) [![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Tw1zT3d2four7/Profilarr)

## Downloads

### Latest Release

- **Download:** [`profilarr-latest.zip`](https://github.com/swvn-dispatch/plugin-repo-dev/releases/download/profilarr-2.1.6/profilarr-2.1.6.zip)
- **Built:** Oct 28 2026, 13:35 UTC
- **Source Commit:** [`f5a6a0b`](https://github.com/swvn-dispatch/plugin-repo-dev/commit/f5a6a0bd3da24796156d458289cd813bf713e9d6)

**Checksums:**
```
MD5:    6c9603f09f266b707cbf92d05b2edb5f
SHA256: c9ee48397f689b11d6b8fe0a01f31418ddcb0dc20c575f42c8e4feb25282ca2f
```

### All Versions

| Version | Download | Built | Commit | MD5 | SHA256 |
|---------|----------|-------|--------|-----|--------|
| `2.1.6` | [Download](https://github.com/swvn-dispatch/plugin-repo-dev/releases/download/profilarr-2.1.6/profilarr-2.1.6.zip) | Oct 28 2026, 13:35 UTC | [`f5a6a0b`](https://github.com/swvn-dispatch/plugin-repo-dev/commit/f5a6a0bd3da24796156d458289cd813bf713e9d6) | 6c9603f09f266b707cbf92d05b2edb5f | c9ee48397f689b11d6b8fe0a01f31418ddcb0dc20c575f42c8e4feb25282ca2f |

---

**Maintainers:** Tw1zT3d2four7 | **Source:** [Browse Plugin](https://github.com/swvn-dispatch/plugin-repo-dev/tree/main/plugins/profilarr)

**Metadata:** [View full manifest](./manifest.json)

---

## Plugin README

# Profilarr

Hybrid ffmpeg + cvlc stream profiles. ffmpeg fetches the provider stream directly with a custom user-agent and reconnect handling, and regenerates timestamps (+genpts+igndts+discardcorrupt, resent PAT/PMT, clamped negative timestamps); cvlc then buffers and delivers that already-clean stream, so downstream players don't freeze on a CDN-hiccup discontinuity.

Full docs, install options, and troubleshooting: https://github.com/Tw1zT3d2four7/Profilarr
