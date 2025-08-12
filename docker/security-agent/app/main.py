import requests
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Security Agent Running")

def run(server_class=HTTPServer, handler_class=HealthCheckHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting security agent on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
