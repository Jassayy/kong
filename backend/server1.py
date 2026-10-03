from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/hello":
            headers = {
                key: value
                for key, value in self.headers.items()
            }
            response = {
                "message": "Hello from Backend 1",
                "server": "backend-1",
                "headers": headers
            }

            body = json.dumps(response).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(body))
            self.end_headers()

            self.wfile.write(body)

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 9001), Handler)

print("Backend 1 running on port 9001")

server.serve_forever()