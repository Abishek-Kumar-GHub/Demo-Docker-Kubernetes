from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 80

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Docker Python Container!")

server = HTTPServer(("", PORT), HelloHandler)
print(f"Serving on port {PORT}")
server.serve_forever()
