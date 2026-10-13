"""Static CodeQL fixture. This function is never invoked."""

import subprocess


def suppressed_capability_use():
    # codeql[plugin/capability-contract/subprocess]
    subprocess.run(["true"])
