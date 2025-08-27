#!/usr/bin/env python3
"""Simple server for testing the portfolio locally"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"🌐 Starting portfolio server on http://localhost:{PORT}")
print("📁 Serving files from:", DIRECTORY)
print("Press Ctrl+C to stop the server\n")

# Open in browser
webbrowser.open(f'http://localhost:{PORT}')

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    httpd.serve_forever()
