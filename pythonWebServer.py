from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET requests
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes("<html><head><title>My Web Server</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: GET %s</p>" %
                             self.path, "utf-8"))
            self.wfile.write(
                bytes("<p>This is an example web server GET operation.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Not Found", "utf-8"))

    def do_POST(self):
        # Handle POST requests
        if self.path == "/submit":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            # Parse form data (assuming it's a simple key-value pair)
            form_data = cgi.parse_qs(post_data)
            name = form_data.get("name", [""])[0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(f"<html><head><title>Submitted Data</title></head>", "utf-8"))
            self.wfile.write(
                bytes(f"<p>Received POST request with name: {name}</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Not Found", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
