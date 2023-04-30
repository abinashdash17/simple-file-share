import qrcode
import io
import sys
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler


def get_ip_addr(num):
    # hostname = socket.gethostname()
    # ip_addr = socket.gethostbyname(hostname)
    addrs = socket.getaddrinfo(socket.gethostname(), None)
    ip_addr = []
    for addr in addrs:
        ip = addr[4][0]
        if ip.startswith("192"):
            ip_addr.append(ip)
    print("Network interfaces:" + str(len(ip_addr)))
    print("Using Network interface :" + str(num))
    try:
        return ip_addr[num - 1]
    except:
        print("invalid network interface, can't print qr code")
        sys.exit(1)


nw_interface_id = 2
change_bg_color = False
if len(sys.argv) > 1:
    change_bg_color = True
sys.tracebacklimit = 0  # comment this line to debug errors/warnings
print()
url = "http://" + get_ip_addr(nw_interface_id) + ":8000"
print("Visit the below link or use the qr: ")
print(url)
print("Use the 2nd QR code, if the first one doesn't work")


qr = qrcode.QRCode(version=2)
qr.add_data(url)
f = io.StringIO()
qr.print_ascii(out=f, invert=not change_bg_color)
f.seek(0)
print(f.read())

# start server
httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
print("Hit Ctrl+C to stop the server")
httpd.serve_forever()
