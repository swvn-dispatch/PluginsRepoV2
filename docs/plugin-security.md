# Plugin Security Checks

Plugin source is checked before merge in two layers. This repository runs static
analysis while Dispatcharr applies capability checks at runtime for
`manifest_version` 2 and later. Neither layer is a security boundary: plugins
share Dispatcharr's Python interpreter, and the runtime wrappers are defense in
depth.

## Capability Contract Queries

The Python CodeQL pack reports direct use of selected guarded APIs when the
scanned runtime manifest is enforcing and omits the matching capability:

| Rule | Detection |
|---|---|
| `subprocess` | `subprocess` process-launch APIs without `subprocess` |
| `network-listener` | Socket bind/listen calls without `network_listener` |
| `outbound-network` | Selected HTTP or socket connection calls without `outbound_network` |

`pluginctl.capabilities` mirrors Dispatcharr's capability and manifest-version
policy. Versions 0 and 1 do not produce contract findings. Future manifest
versions use the latest known policy, as Dispatcharr does. Unknown future
capabilities remain valid declarations. For external plugins, the scan saves the
release manifest separately from catalog metadata. A catalog `plugin.json`
without a `manifest_version` is not treated as a runtime manifest.

## Sandbox Bypass Queries

The pack separately detects concrete attempts to undermine the current
plugin-local builtins and import wrappers:

| Rule | Detection |
|---|---|
| `sys-modules-tamper` | Replacement of sensitive `sys.modules` entries |
| `ctypes-usage` | Native-code access through `ctypes` |
| `builtins-mutation` | Mutation of `__builtins__` |

The broad frame, introspection, and dynamic-evaluation heuristics from the
earlier query pack were removed because they do not model Dispatcharr's current
`ContextVar` and plugin-local builtins design.

Both query families are informational to required validation. A contract finding,
bypass finding, or CodeQL suppression applies `Manual Review Required`, which
blocks automatic merging until a maintainer reviews the PR. Removing the detected
code clears the label on the next validation run.

## Suppressions

Use an inline `codeql[rule-id]` suppression only for a justified exception. A
suppressed result still applies `Manual Review Required` and blocks automatic
merge.
