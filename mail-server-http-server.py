#!/usr/bin/env python3

import http.server
import cgi
import os
import threading
from socketserver import ThreadingMixIn
import json
import ssl
import mailClient

#import smtplib for sending the email ie.  Connect as a client to a email server
# import smtplib

#import any email modules needed to construct headers and format the email itself
# from email.mime.text import MIMEText


# Instanstiate a thread ready server for processing request when ready
class ThreadHTTPServer (ThreadingMixIn, http.server.HTTPServer):
    "This adds thread-based concurrency"

# create a base request handler to provide logic for responding to post requests

class EmailResponder(http.server.BaseHTTPRequestHandler):

    def do_POST(self):

        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")

        if ctype == 'multipart/form-data':
            self.send_response(201)
            self.send_header('Content-Type','application/json')
            self.send_header('Access-Control-Allow-Credentials','true')
            self.send_header('Access-Control-Allow-Origin','http://localhost:4000')
            self.send_header('Access-Control-Expose-Headers', 'AMP-Access-Control-Allow-Source-Origin')
            self.send_header('AMP-Access-Control-Allow-Source-Origin', 'http://localhost:4000')
            self.end_headers()

            # get useful fields from the request 
            fields = cgi.parse_multipart(self.rfile, pdict)
            first_name = fields.get('First_Name')[0].decode()
            last_name = fields.get('Last_Name')[0].decode()
            email_address = fields.get('Email_Address')[0].decode()
            telephone_number = fields.get('Telephone_Number')[0].decode()
            json_response = json.dumps({'email_address': email_address,'first_name':first_name, 'last_name':last_name})
            self.wfile.write(bytes(json_response, 'utf-8'))
            print(first_name)
            mailClient.send(first_name, last_name, email_address, telephone_number)
            

if __name__ == '__main__':
    port = int(os.environ.get('PORT',8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, EmailResponder)
    httpd.socket=ssl.wrap_socket(httpd.socket, certfile = '/Users/dan/.certs/server.pem', server_side=True)
    httpd.serve_forever()
