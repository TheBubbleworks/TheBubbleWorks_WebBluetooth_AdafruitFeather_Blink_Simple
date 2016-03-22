#!/usr/bin/env python

import BaseHTTPServer, SimpleHTTPServer
import ssl

#To gerneate a new server certificate:
#   openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes

httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 9443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.pem', server_side=True)
httpd.serve_forever()

