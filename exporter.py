#!/usr/bin/env python

import vici
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    strongswan_session = vici.Session()

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def _sas_len_iter(self, list_sas):
        for this_sas in list_sas:
            ikev2 = this_sas['ikev2']
            child_sas = ikev2['child-sas']
            yield len(child_sas)

    def _strongswan_connections_iter(self):
        list_sas = self.strongswan_session.list_sas()
        strongswan_connections = sum(self._sas_len_iter(list_sas))
        yield '# HELP strongswan_connections Number of strongswan connections.'
        yield '# TYPE strongswan_connections gauge'
        yield 'strongswan_connections %s' % strongswan_connections

    def _messages_iter(self):
        yield from self._strongswan_connections_iter()

    def do_GET(self):
        self._set_headers()
        for message in self._messages_iter():
            self.wfile.write(message.encode())
            self.wfile.write(b'\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="HTTP Host Name",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=9000,
        help="HTTP Port",
    )

    args = parser.parse_args()

    server_address = (args.host, args.port)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()
