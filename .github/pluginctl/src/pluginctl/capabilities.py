"""Dispatcharr plugin capability and manifest-schema compatibility policy.

This intentionally mirrors ``apps.plugins.capabilities`` in Dispatcharr without
depending on Django or plugin loading. Keep capability/version semantics aligned
with Dispatcharr; ``codeql_rules`` is registry-only metadata for this repository.
"""

from __future__ import annotations

from typing import Any


CAPABILITY_GROUPS: dict[str, dict[str, Any]] = {
    "system": {"label": "System", "order": 0},
    "network": {"label": "Network", "order": 1},
    "storage": {"label": "Storage", "order": 2},
    "data": {"label": "Data", "order": 3},
    "other": {"label": "Other", "order": 99},
}

KNOWN_CAPABILITIES: dict[str, dict[str, Any]] = {
    "background_tasks": {
        "group": "system",
        "label": "Run background tasks",
        "description": "Runs long-running or scheduled work on Dispatcharr's shared background task queue.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": True,
        "codeql_rules": ["plugin/capability-contract/background-tasks"],
    },
    "persistent_service": {
        "group": "system",
        "label": "Run a persistent background service",
        "description": "Elected as a cluster-wide leader to run a long-lived service.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": True,
        "codeql_rules": ["plugin/capability-contract/persistent-service"],
    },
    "network_listener": {
        "group": "network",
        "label": "Listen for network connections",
        "description": "Binds a socket or web server that accepts inbound network connections.",
        "requires_restart": True,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": True,
        "codeql_rules": ["plugin/capability-contract/network-listener"],
    },
    "subprocess": {
        "group": "system",
        "label": "Run host processes",
        "description": "Starts commands or processes on the Dispatcharr host.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": True,
        "codeql_rules": ["plugin/capability-contract/subprocess"],
    },
    "outbound_network": {
        "group": "network",
        "label": "Access external network services",
        "description": "Connects to remote hosts or makes outbound HTTP requests.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": True,
        "codeql_rules": ["plugin/capability-contract/outbound-network"],
    },
    "filesystem_write": {
        "group": "storage",
        "label": "Write outside plugin storage",
        "description": "Writes files outside the plugin's code and persistent data directories.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": True,
        "codeql_rules": [],
    },
    "celery_dispatch": {
        "group": "system",
        "label": "Dispatch approved internal tasks",
        "description": "Queues explicitly approved Dispatcharr background tasks.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": True,
        "codeql_rules": ["plugin/capability-contract/celery-dispatch"],
    },
    "proxy_internals": {
        "group": "data",
        "label": "Use live proxy internals",
        "description": "Uses Dispatcharr live-stream proxy implementation details.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": False,
        "codeql_rules": [],
    },
    "user_data": {
        "group": "data",
        "label": "Access user account data",
        "description": "Reads Dispatcharr user account data.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": False,
        "codeql_rules": [],
    },
    "external_dependencies": {
        "group": "system",
        "label": "Install external Python dependencies",
        "description": "Installs declared third-party Python packages for this plugin.",
        "requires_restart": False,
        "min_manifest_version": 1,
        "max_manifest_version": None,
        "runtime_enforced": False,
        "codeql_rules": [],
    },
}

MANIFEST_SCHEMA_POLICIES: dict[int, dict[str, bool]] = {
    0: {"parses_capabilities": False, "enforces_sandbox": False},
    1: {"parses_capabilities": True, "enforces_sandbox": False},
    2: {"parses_capabilities": True, "enforces_sandbox": True},
}


def parse_manifest_version(manifest: dict[str, Any]) -> int:
    try:
        value = int(manifest.get("manifest_version", 0))
    except (TypeError, ValueError):
        return 0
    return value if value >= 0 else 0


def manifest_schema_policy(manifest_version: int) -> dict[str, bool]:
    return MANIFEST_SCHEMA_POLICIES.get(
        manifest_version, MANIFEST_SCHEMA_POLICIES[max(MANIFEST_SCHEMA_POLICIES)]
    )


def manifest_version_parses_capabilities(manifest_version: int) -> bool:
    return manifest_schema_policy(manifest_version)["parses_capabilities"]


def manifest_version_enforces_sandbox(manifest_version: int) -> bool:
    return manifest_schema_policy(manifest_version)["enforces_sandbox"]


def first_enforcing_manifest_version() -> int:
    return min(
        version for version, policy in MANIFEST_SCHEMA_POLICIES.items()
        if policy["enforces_sandbox"]
    )


def capability_supported_by_manifest_version(capability_id: str, manifest_version: int) -> bool:
    if not manifest_version_parses_capabilities(manifest_version):
        return False
    policy = KNOWN_CAPABILITIES.get(capability_id)
    if policy is None:
        return True
    minimum = policy["min_manifest_version"]
    maximum = policy["max_manifest_version"]
    return (minimum is None or manifest_version >= minimum) and (
        maximum is None or manifest_version <= maximum
    )


def declared_capabilities(manifest: dict[str, Any]) -> set[str]:
    version = parse_manifest_version(manifest)
    values = manifest.get("capabilities")
    if not isinstance(values, list):
        return set()
    return {
        value for value in values
        if isinstance(value, str) and capability_supported_by_manifest_version(value, version)
    }
