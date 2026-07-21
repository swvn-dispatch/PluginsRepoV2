[Back to All Plugins](../../README.md)

# reservoarr

**Version:** `6.3.1` | **Author:** brko7 | **Last Updated:** Jul 03 2026, 16:10 UTC

Delay-buffer stream profile that absorbs IPTV CDN gaps so Plex Live TV stops dying

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://spdx.org/licenses/MIT.html) [![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/brko7/reservoarr)

![Dispatcharr min](https://img.shields.io/badge/Dispatcharr_min-v0.25.0-brightgreen?style=flat-square)

## Downloads

### Latest Release

- **Download:** [`reservoarr-latest.zip`](https://github.com/swvn-dispatch/PluginsRepoV2/releases/download/reservoarr-6.3.1/reservoarr-6.3.1.zip)
- **Built:** Jul 21 2026, 17:42 UTC
- **Source Commit:** [`87eb446`](https://github.com/swvn-dispatch/PluginsRepoV2/commit/87eb4462b4d69c9c7fed119696b027be4b6ed2c2)

**Checksums:**
```
MD5:    8a7ad55909de876961f97c680544f5a8
SHA256: 87639f84417d02b06649466f287fa6e9ad28a5255b7e34e4b721cc49bec5d73b
```

### All Versions

| Version | Download | Built | Commit | MD5 | SHA256 |
|---------|----------|-------|--------|-----|--------|
| `6.3.1` | [Download](https://github.com/swvn-dispatch/PluginsRepoV2/releases/download/reservoarr-6.3.1/reservoarr-6.3.1.zip) | Jul 21 2026, 17:42 UTC | [`87eb446`](https://github.com/swvn-dispatch/PluginsRepoV2/commit/87eb4462b4d69c9c7fed119696b027be4b6ed2c2) | 8a7ad55909de876961f97c680544f5a8 | 87639f84417d02b06649466f287fa6e9ad28a5255b7e34e4b721cc49bec5d73b |

---

**Maintainers:** brko7 | **Source:** [Browse Plugin](https://github.com/swvn-dispatch/PluginsRepoV2/tree/main/plugins/reservoarr)

**Metadata:** [View full manifest](./manifest.json)

---

## Plugin README

# reservoarr

A delay-buffer **stream profile** that absorbs IPTV CDN gaps so Plex Live TV stops dying. Eagerly drains the upstream into a RAM reservoir, then releases bytes to ffmpeg at the stream's PCR-derived content rate. Playback runs ~30s behind live, and gaps shorter than the cushion are invisible to the player.

## What this is for

- Your IPTV provider's CDN has prime-time gaps, occasional EOFs, or per-connection corrupt-loops.
- You watch through **Plex Live TV** (~15s tuner timeout) or any consumer that's strict about input continuity.
- Symptoms today: channels die mid-stream, won't tune on first try, A/V desync after a reconnect, short black-frame stutters.

If your provider streams cleanly, you don't need this.

## Install

Dispatcharr → Plugins → **Find Plugins** → search "reservoarr" → Install. Click **Generate Stream Profile** in the plugin settings.

Tuning is via `RESV_*` environment variables on the Dispatcharr container — see the [TUNABLES doc](https://github.com/brko7/reservoarr/blob/main/docs/TUNABLES.md). Defaults match production-validated behaviour and fit most providers.

## Architecture (one paragraph)

`upstream HTTP` → RAM reservoir (≤256MB, ~30s target cushion) → byte-rate paced release at the PCR content rate → ffmpeg remux (video copy + `dump_extra` + `-c:a ac3`) → Dispatcharr → Plex. Pacing happens in the wrapper, **not** with `ffmpeg -re` — the provider's streams carry occasional corrupt packets with garbage DTS, and `-re` sleeps on them. PCR is a *measurement* input; a garbage sample is rejected by a plausibility window. Three watchdogs ride alongside (corrupt-loop, stall, TS-corruption).

## Telemetry

`/data/scripts/logs/delaybuf.log` (configurable, self-rotates at 10 MB):

```
2026-06-14T10:03:33 [500004175] cushion=27s(pcr) buf=15.5MB out=4.66Mbps in=4.96Mbps crate=4.80Mbps in_total=1843MB reconnects=0 ccerr=0 pcrrej=0 disc=0 sync=0
```

Full schema in the [TELEMETRY doc](https://github.com/brko7/reservoarr/blob/main/docs/TELEMETRY.md).

## More

- Source, issues, discussions: https://github.com/brko7/reservoarr
- Releases: https://github.com/brko7/reservoarr/releases
- Hard invariants (every one earned by a production failure): https://github.com/brko7/reservoarr/blob/main/docs/INVARIANTS.md

MIT licensed.
