"""Replica of icanhazip.com - WSGI Style"""

from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults


def ip_app(environ, start_response):
    setup_testing_defaults(environ)

    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    return ['{0}'.format(environ['REMOTE_ADDR']).encode('UTF-8')]


if __name__ == '__main__':
    make_server('0.0.0.0', 8000, ip_app).serve_forever()