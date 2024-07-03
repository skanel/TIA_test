import http.server
import socketserver
import threading

# List of ports to run servers on
PORTS = [8001, 8002, 8003, 8004]

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.port = kwargs.pop('port')
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"Handled by server on port {self.port}".encode())

def run_server(port):
    with socketserver.TCPServer(("127.0.0.1", port), lambda *args, **kwargs: Handler(*args, port=port, **kwargs)) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()

# Start a server on each port in the list
for port in PORTS:
    threading.Thread(target=run_server, args=(port,)).start()
