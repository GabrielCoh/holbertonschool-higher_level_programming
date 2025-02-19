#!/usr/bin/python3
"""Develop a simple API using Python with the 'http.server' module"""


from http.server import Base HTTPRequestHandler, HTTPServer
import json


class MyRequestHandler(BaseHTTPRequestHandler):
    """Class MyRequestHandler"""
    def send_text(self, data, status=200):
        """Function to send text responses"""
        self.send_response(status)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

    def send_json(self, data, status=200):
        """Function to send JSON responses"""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """Function that handles GET Requests"""
        if self.path == '/':
            self.send_text("Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == '/status':
            self.send_text("OK")
        elif self.path == '/info':
            self.send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
                })
        else:
            self.send_text("Endpoint not found", 404)


def run_server(host="localhost", port=8000):
    """Starts the server"""
    with HTTPServer((host, port), RequestHandler) as web_server:
        print("Starting server on http://{}:{}".format(host, port))

        try:
            web_server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            web_server.server_close()
            print("\nServer stopped")


if __name__ == "__main__":
    run_server()
