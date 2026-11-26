from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        msg = params.get('msg', ['Hello, World! V2'])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = f"<html><body><h1>GET: {msg}</h1></body></html>"
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        # อ่านขนาดและข้อมูลที่ส่งมาจาก Client
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # แสดงข้อมูลที่ได้รับทางหน้าจอ Terminal ของ Server
        print(f"ได้รับข้อมูล POST จาก Client: {post_data}")

        # ส่งคำตอบกลับไปยัง Client
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        response = f"Server ได้รับข้อมูล POST เรียบร้อย: {post_data}"
        self.wfile.write(response.encode('utf-8'))

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print("Server running on port 8000...")
    httpd.serve_forever()