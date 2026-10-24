import requests
import socket
import http.client

requests.get("https://example.com")
socket.create_connection(("example.com", 443))
socket.socket().connect(("example.com", 443))
http.client.HTTPSConnection("example.com")
