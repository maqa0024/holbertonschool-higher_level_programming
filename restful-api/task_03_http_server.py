#!/usr/bin/env python3
"""Simple HTTP API server using the http.server standard library module."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

ROUTES = {
    "/": ("text/plain", "Hello, this is a simple API!"),
    "/status": ("text/plain", "OK"),
    "/data": ("application/json", {"name": "John", "age": 30, "city": "New York"}),
    "/info": ("application/json", {"version": "1.0", "description": "A simple API built with http.server"}),
}


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests and route to the appropriate endpoint."""

    def do_GET(self):
        if self.path not in ROUTES:
            self._respond(404, "text/plain", "Endpoint not found")
            return

        content_type, payload = ROUTES[self.path]

        if isinstance(payload, dict):
            body = json.dumps(payload)
        else:
            body = payload

        self._respond(200, content_type, body)

    def _respond(self, status_code, content_type, body):
        encoded = body.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, fmt, *args):
        """Override to produce cleaner single-line log output."""
        print(f"{self.address_string()} - {fmt % args}")


if __name__ == "__main__":
    server = HTTPServer(("", PORT), SimpleAPIHandler)
    print(f"Server running on http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
