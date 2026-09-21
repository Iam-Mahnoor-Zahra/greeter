from http.server import BaseHTTPRequestHandler, HTTPServer

HTML = """<!DOCTYPE html>
<html>
  <head><title>Hello</title></head>
  <body style="font-family: sans-serif; text-align: center; margin-top: 20vh;">
    <h1>Hi, Mahnoor! 👋</h1>
    <p>Theories Dissolve when the Loss becomes yours</p>
  </body>
</html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

if __name__ == "__main__":
    print("Open http://localhost:8000 in your browser")
    HTTPServer(("", 8000), Handler).serve_forever()