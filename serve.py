#!/usr/bin/env python3
"""
DENSO Course — Local Dev Server
Run: python3 serve.py
Then open: http://localhost:8000
"""
import http.server, socketserver, os, sys

PORT = 8000
# Serve from the directory you pass as argument, or current directory
directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)
    def log_message(self, format, *args):
        # Clean log output
        print(f"  {self.address_string()} → {args[0]}")

print(f"\n  DENSO Dev Server")
print(f"  Serving: {directory}")
print(f"  URL:     http://localhost:{PORT}")
print(f"  Stop:    Ctrl+C\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
