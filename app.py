from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({k: v for k, v in os.environ.items()}, sort_keys=True).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        return

HTTPServer(("0.0.0.0", 8000), H).serve_forever()
