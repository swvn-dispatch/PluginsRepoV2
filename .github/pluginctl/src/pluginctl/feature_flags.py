"""Hardcoded rollout switches for trusted pluginctl automation."""

# Neither family fails required validation. Both are review-gated through PR
# labels, and must not be environment-configurable by untrusted PR code.
CAPABILITY_CONTRACT_DETECTION = True
SANDBOX_BYPASS_DETECTION = True

SPLIT_MANIFEST_BASE_URLS = False

AI_ASSISTED_MANIFEST_DISCLOSURE = True
