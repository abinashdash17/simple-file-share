import qrcode
import io
import sys
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

sys.tracebacklimit = 0  # comment this line to debug errors/warnings
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

url = "http://" + ip_addr + ":8000"
print()
print("Visit the below link or use the qr: ")
print(url)
print("Use the 2nd QR code, if the first one doesn't work")


# generate qr code in light bg
qr1 = qrcode.QRCode(version=3)
qr1.add_data(url)
f = io.StringIO()
qr1.print_ascii(out=f, invert=True)
f.seek(0)
print(f.read())

# generate qr code in light bg
qr2 = qrcode.QRCode(version=3)
qr2.add_data(url)
f = io.StringIO()
qr2.print_ascii(out=f)
f.seek(0)
print(f.read())

# start server
httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
print("Hit Ctrl+C to stop the server")
httpd.serve_forever()
