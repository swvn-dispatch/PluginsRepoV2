[Back to All Plugins](../../README.md)

# EPG Janitor

**Version:** `1.26.2281111` | **Author:** PiratesIRC | **Last Updated:** Aug 16 2026, 16:17 UTC

Scans for channels with EPG assignments but no program data. Auto-matches EPG to channels using intelligent fuzzy matching with aliases, removes EPG from hidden channels, and manages EPG assignments.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://spdx.org/licenses/MIT.html) [![Discord](https://img.shields.io/badge/Discord-Discussion-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.com/channels/1340492560220684331/1420051973994053848) [![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PiratesIRC/Dispatcharr-EPG-Janitor-Plugin)

![Dispatcharr min](https://img.shields.io/badge/Dispatcharr_min-v0.20.0-brightgreen?style=flat-square)

## Downloads

### Latest Release

- **Download:** [`epg-janitor-latest.zip`](https://github.com/swvn-dispatch/PluginsRepoV2/releases/download/epg-janitor-1.26.2281111/epg-janitor-1.26.2281111.zip)
- **Built:** Aug 22 2026, 23:06 UTC
- **Source Commit:** [`79842f2`](https://github.com/swvn-dispatch/PluginsRepoV2/commit/79842f28375fb5829e2ba64029deb1d60f7c5fb1)

**Checksums:**
```
MD5:    8e7ade420998eadd4c60fcb617672989
SHA256: 239cf4955b3d079ab76c97983a6989472470af7d7cd847b87ac9cabfd8761e30
```

### All Versions

| Version | Download | Built | Commit | MD5 | SHA256 |
|---------|----------|-------|--------|-----|--------|
| `1.26.2281111` | [Download](https://github.com/swvn-dispatch/PluginsRepoV2/releases/download/epg-janitor-1.26.2281111/epg-janitor-1.26.2281111.zip) | Aug 22 2026, 23:06 UTC | [`79842f2`](https://github.com/swvn-dispatch/PluginsRepoV2/commit/79842f28375fb5829e2ba64029deb1d60f7c5fb1) | 8e7ade420998eadd4c60fcb617672989 | 239cf4955b3d079ab76c97983a6989472470af7d7cd847b87ac9cabfd8761e30 |
| `1.26.1791309` | [Download](https://github.com/swvn-dispatch/PluginsRepoV2/releases/download/epg-janitor-1.26.1791309/epg-janitor-1.26.1791309.zip) | Jul 21 2026, 17:41 UTC | [`7ffd2cc`](https://github.com/swvn-dispatch/PluginsRepoV2/commit/7ffd2ccc1e04038873a22979f325ee68773da6e5) | b4350fd30383845dd90afc06531c76b5 | 952d486589fb1b68f518166bc91ed7353361a4c668a2ba9325e40d6c13f73899 |

---

**Maintainers:** PiratesIRC | **Source:** [Browse Plugin](https://github.com/swvn-dispatch/PluginsRepoV2/tree/main/plugins/epg-janitor)

**Metadata:** [View full manifest](./manifest.json)

---

## Plugin README

# EPG Janitor

Keep your Electronic Program Guide clean, accurate, and complete. EPG Janitor operates on channels that already exist in Dispatcharr — it finds broken EPG assignments (no program data), intelligently matches EPGs to channels using callsign/location/network scoring plus a fuzzy pipeline with built-in aliases, and provides bulk cleanup tools for removing EPG from hidden channels or by REGEX.

**Source repo:** https://github.com/PiratesIRC/Dispatcharr-EPG-Janitor-Plugin
**Discord thread:** https://discord.com/channels/1340492560220684331/1420051973994053848

## Requires

Dispatcharr v0.20.0 or newer. Python 3.13+ (bundled). No required dependencies (optionally uses `rapidfuzz` for faster matching if it's present in the environment).

## Key features

- **Auto-Match EPG** — weighted structural scoring (callsign 50 / state 30 / city 20 / network 10) + Lineuparr-style 4-stage fuzzy pipeline (alias → exact → substring → token-sort), takes the higher score. Identical-name matches score 100.
- **Callsign anchoring** — high-confidence US callsign matching for parenthesized (`ABC (WABC)`), end-of-name (`WABC-DT`), and leading `CALLSIGN (NETWORK)` forms (jesmann-US: `KGTV (ABC)`). A shared high-confidence callsign anchors the match; a disagreement rejects a wrong-station candidate. Grandfathered 3-letter callsigns (`(WWL)`, `(WJZ)`) and word-shaped callsigns (`(KING)`, `(WAVE)`) anchor too.
- **Every licensed US station is recognised** — the shipped `us_station_callsigns.json` lists every callsign the FCC licenses, derived from its Licensing and Management System database, and the loaded channel databases add the rest. A callsign-shaped English word such as `KILN` or `WHIP` is never promoted to a station, while a real station whose callsign is also a word is.
- **Sibling guards & smarter normalization** — numbered/time-shift siblings no longer cross-match (`Fox Sports 1`≠`2`, `BBC One`≠`Two`, `ITV2`≠`ITV2 +1`); number-words fold to digits (`BBC Three`=`BBC 3`), CamelCase and dotted compounds split (`97.2` preserved). Similarity is rapidfuzz-parity with optional `rapidfuzz` acceleration.
- **Scan & Heal** — find channels whose current EPG has no program data and walk ranked candidates for a working replacement (respects fallback source allowlist).
- **EPG source selection & priority** — pick eligible sources by name or `*`/`?` wildcard (case-insensitive); only enabled sources are used, and score ties resolve by each source's Dispatcharr `priority` (higher wins). Leave it empty and *all* active sources are eligible — including foreign-country ones (the matcher has no country gate), so scope it to your region (e.g. `*-US`) on single-region installs.
- **~200 built-in aliases** (FS1/FS2, CSPAN variants, rebrands like EPIX→MGM+, MSNBC→MS NOW, getTV→GREATTV, DIY→Magnolia, Hallmark Movies & Mysteries→Hallmark Mystery, Justice Network→True Crime Network). User-extendable via a JSON `custom_aliases` setting.
- **Regional differentiation** (East/West/Pacific, Pacific ≡ West) — lineup channels with regional markers only match compatible EPG feeds, even when `ignore_regional_tags=true`.
- **Per-category normalization toggles** — quality (`[HD]`, `[4K]`), regional (East/West/Pacific), geographic (`US:`, `[CA]`), misc (`(A)`, `(CX)`) stripped independently.
- **Performance** — pre-normalization cache + per-EPG attribute cache. ~7–8 min for a 21,480-EPG × 2,950-channel run.
- **Bulk management** — remove EPG by REGEX, from hidden channels, or from entire groups. Tag channels with missing program data via configurable suffix.
- **CSV exports** — every dry-run and apply exports results with confidence scores, match method, and reasoning.
- **EPG Freshness Watchdog (optional, off by default)** — Dispatcharr's own EPG refresh has no retry and no freshness awareness, so a source that fails, or whose guide data simply runs out, stays broken until somebody notices. On a schedule you set, the watchdog checks every active source that has channels mapped to it and refreshes any that has errored or is close to running out of guide data. It records system events only. There is no webhook, no email and no network code of any kind. A button runs the same check immediately.

## Settings

Organized into sections via UI dividers: Scope, Auto-Match, Scan & Heal, Cleanup & Maintenance, Normalization Toggles, Custom Aliases, and EPG Freshness Watchdog. Dynamic per-country channel-database toggles (US, UK, CA, DE, ES, FR, IN, MX, NL, AU, BR, NO) auto-generated based on shipped `*_channels.json` files.

## Actions

15 color-coded action buttons grouped by destructiveness (blue outlines for info, cyan for dry-runs, green-filled for apply-style, orange/red-filled for destructive) with confirmation dialogs on anything that mutates channel state. Emoji labels.

## How it differs from other matching plugins

- **Not a channel creator.** EPG Janitor does not create channels or scan M3U sources — it works on channels you already have in Dispatcharr. For provider-lineup-driven channel creation see [Lineuparr](https://github.com/PiratesIRC/Dispatcharr-Lineuparr-Plugin).
- **EPG-first matching.** The weighted pipeline is tuned for matching EPG entries (which often carry callsigns + geographic context for US broadcast) rather than IPTV stream names.
- **Heal semantics.** First-class support for replacing broken EPG assignments with working ones — walks ranked candidates and validates program-data availability before applying.

## Install

Install directly from the Dispatcharr Plugin Hub (search for **EPG Janitor**), or download the latest release from the source repo and import via **Plugins → Import Plugin** in the Dispatcharr UI.

## License

MIT © 2026 PiratesIRC

---

*All product names, trademarks, and registered trademarks mentioned in this project are the property of their respective owners. Channel alias data is community-compiled from publicly available information and is not affiliated with or endorsed by any broadcaster.*
