"""Static CodeQL fixture. None of these functions are invoked."""

import socket
import subprocess
import urllib.request

import requests


def use_undeclared_capabilities(context):
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen()
    subprocess.run(["true"])
    requests.get("https://example.com")
    urllib.request.urlopen("https://example.com")
    context["dispatch_task"]("fixture")
    context["dispatch_internal_task"]("fixture")


def on_leader_acquired():
    return None
