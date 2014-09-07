"""Replica of icanhazepoch.com - HTTP Style"""

from time import time
from wsgiref.simple_server import BaseHTTPRequestHandler, HTTPServer
# Dirty import, but works both on Python 2 and Python 3


class EpochHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write('{0:.0f}'.format(time()).encode('UTF-8'))

if __name__ == '__main__':
    HTTPServer(('0.0.0.0', 8000), EpochHandler).serve_forever()