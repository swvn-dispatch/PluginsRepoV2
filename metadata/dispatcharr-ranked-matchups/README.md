[Back to All Plugins](../../README.md)

# Ranked Matchups (Top Games)

**Version:** `1.36.0` | **Author:** Jacob-Lasky | **Last Updated:** Oct 16 2026, 14:29 UTC

Never miss a good game. Scores every upcoming game across 39 leagues, tours and competitions (22 of them soccer, plus NFL, NBA, MLB, NHL, NCAA D1 football and basketball, UFC, boxing, tennis, golf and motorsport), then builds a Top Matchups group holding only the ones worth watching and shows why each game ranked where it did in its EPG description. Finished games can clear themselves out and be replaced from a bench of the next-best fixtures.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://spdx.org/licenses/MIT.html) [![Discord](https://img.shields.io/badge/Discord-Discussion-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.com/channels/1340492560220684331/1508938899865604167) [![Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Jacob-Lasky/dispatcharr_ranked_matchups)

## Downloads

### Latest Release

- **Download:** [`dispatcharr-ranked-matchups-latest.zip`](https://github.com/swvn-dispatch/plugin-repo-dev/releases/download/dispatcharr-ranked-matchups-1.36.0/dispatcharr-ranked-matchups-1.36.0.zip)
- **Built:** Oct 28 2026, 13:34 UTC
- **Source Commit:** [`aaac7b4`](https://github.com/swvn-dispatch/plugin-repo-dev/commit/aaac7b46076be8379e4bc9a0adc97e51807401c5)

**Checksums:**
```
MD5:    10f714d203c969838e1e0b4fa5fae8bd
SHA256: 4d3aa5843174a8cc708d8b3846af52e3f1c1dda968af71138ad21ee6e3f0a61a
```

### All Versions

| Version | Download | Built | Commit | MD5 | SHA256 |
|---------|----------|-------|--------|-----|--------|
| `1.36.0` | [Download](https://github.com/swvn-dispatch/plugin-repo-dev/releases/download/dispatcharr-ranked-matchups-1.36.0/dispatcharr-ranked-matchups-1.36.0.zip) | Oct 28 2026, 13:34 UTC | [`aaac7b4`](https://github.com/swvn-dispatch/plugin-repo-dev/commit/aaac7b46076be8379e4bc9a0adc97e51807401c5) | 10f714d203c969838e1e0b4fa5fae8bd | 4d3aa5843174a8cc708d8b3846af52e3f1c1dda968af71138ad21ee6e3f0a61a |

---

**Source:** [Browse Plugin](https://github.com/swvn-dispatch/plugin-repo-dev/tree/main/plugins/dispatcharr-ranked-matchups)

**Metadata:** [View full manifest](./manifest.json)

---

## Plugin README

# Ranked Matchups (Top Games)

A cross-sport "interestingness" curator for Dispatcharr. It pulls upcoming games for each sport you enable, scores every matchup on how interesting it is (rankings, standings, rivalries, betting lines, playoff/knockout stakes), matches the worthwhile games against your lineup, and renames + groups them into a dedicated **!Top Matchups** channel group. Your guide ends up showing the games worth watching instead of the full firehose.

## What it does

- Per-sport adapters (college football/basketball, NFL, NBA, MLB, NHL, WNBA, NWSL, MLS, top-flight soccer leagues, internationals/friendlies, World Cup, and more), each toggleable.
- Scores matchups with a transparent model (see `SCORING.md` in the source repo): ranked-vs-ranked, standings importance, rivalries, and betting-line signal where available.
- Matches scored games against your lineup and builds a curated **!Top Matchups** channel group with clean, renamed entries.
- Runs on demand from the plugin UI or on a schedule.

## How games are matched

Three independent paths, all of which can contribute (results merge and stack as
fallback streams):

- **EPG programme title, sub-title or description** inside the game's window.
- **Channel name**, for providers that name the fixture on the channel.
- **Stream name, whether or not that stream is attached to a channel.** This is
  what lets a large M3U produce per-match feeds without curating them into
  channels first, and it is why a matchup channel can pick up feeds you never
  added yourself.

Because that third path sweeps your whole M3U, three settings decide what
happens to feeds you did not curate, and none of them removes a stream unless
you say so: **Preferred languages** (an ordered list like `en` or `de, en`),
**Demote stream groups** (used only as a last resort, still playable), and
**Exclude stream groups** (never attached at all). Streams you have attached to
a channel of your own always sort ahead of ones found only by the sweep.

## Requirements

- Most sources need a free API key (e.g. CollegeFootballData / CollegeBasketballData, Football-Data.org, The Odds API). Each sport's setting documents which key it needs; sports you do not enable need no key.
- Off-season sports simply produce no rows.

## Source, docs, and issues

Full source, scoring methodology, changelog, and issue tracker live in the upstream repository:

https://github.com/Jacob-Lasky/dispatcharr_ranked_matchups

## License

MIT
