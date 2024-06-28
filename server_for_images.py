from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os
import glob

class CustomHandler(SimpleHTTPRequestHandler):
    def _set_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')

    def send_response(self, code, message=None):
        SimpleHTTPRequestHandler.send_response(self, code, message)
        self._set_cors_headers()

    def do_GET(self):
        if self.path == '/latest-images':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Get the four most recent image files
            files = sorted(glob.glob("*.jpg"), key=os.path.getmtime, reverse=True)[:4]
            self.wfile.write(json.dumps(files).encode())
        else:
            # Serve static files for any other requests
            super().do_GET()

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()


if __name__ == "__main__":
    os.chdir('/home/louis/camera_script')  # Change to your images directory
    run()
