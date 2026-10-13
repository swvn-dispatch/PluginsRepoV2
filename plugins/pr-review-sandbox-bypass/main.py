"""Static CodeQL fixture. None of these functions are invoked."""

import asyncio
import builtins
import ctypes
import importlib
import io
import os
import socket
import sys

import requests


def attempt_wrapper_bypasses():
    sys.modules["subprocess"] = object()
    __builtins__["open"] = lambda *args, **kwargs: None
    builtins.open("/tmp/fixture.txt", "w")
    importlib.import_module("subprocess")
    socket.create_connection(("127.0.0.1", 9))
    requests.Session()
    os.system("true")
    asyncio.create_subprocess_exec("true")
    io.open("/tmp/fixture.txt", "w")
    return ctypes
