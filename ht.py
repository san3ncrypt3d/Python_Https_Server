import ssl, socketserver
from http.server import HTTPServer, SimpleHTTPRequestHandler 

cert = "san3.pem"
httpd = socketserver.TCPServer(('10.0.0.140', 443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=cert,
certfile=cert, server_side=True) 

httpd.serve_forever()
