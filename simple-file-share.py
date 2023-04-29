import qrcode
import io
import sys
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

sys.tracebacklimit = 0 # comment this line to debug errors/warnings
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

url = 'http://'+ip_addr+':8000'
print()
print('Visit the below link or use the qr: ')
print(url)

qr = qrcode.QRCode(version=3)
qr.add_data(url)
f=io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
print('Hit Ctrl+C to stop the server')
httpd.serve_forever()