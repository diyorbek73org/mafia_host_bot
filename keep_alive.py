from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def keep_alive():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

def start():
    t = threading.Thread(target=keep_alive)
    t.daemon = True
    t.start()
