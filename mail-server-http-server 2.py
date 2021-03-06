#!/usr/bin/env python3



import http.server
import cgi
import os
import threading
from socketserver import ThreadingMixIn

# turn up amount of excepions
# import cgitb
# cgitb.enable()

#import smtplib for sending the email ie.  Connect as a client to a email server
import smtplib

#import any email modules needed to construct headers and format the email itself
from email.mime.text import MIMEText


# Instanstiate a thread ready server for processing request when ready
class ThreadHTTPServer (ThreadingMixIn, http.server.HTTPServer):
    "This adds thread-based concurrency"

# create a base request handler to provide logic for responding to post requests

class EmailResponder(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        # Decode the form data.
        # length = int(self.headers.get('Content-length', 0))
        # body = self.rfile.read(length).decode()
        # ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        # print(self.headers)
        # print(self.headers.keys())
        # print(self.headers.get('content-type'))
        # cytpe, pdict, pdict1 =  self.headers.get('content-type')
        ct = self.headers.get('content-type')
        print(ct)
        # print(self.headers.get_content_subtype())
        # ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        # post_variables = cgi.parse_multipart(self.rfile, pdict)
        # print(post_variables)

        # print(ctype)
        # pdict.keys()
        # pdict.values()
        # pdict['form-data']
        # pdict['form-data']
        # pdict['content-type']
        # post_variables = cgi.parse_multipart(self.rfile, pdict)
        # print(post_variables)



if __name__ == '__main__':
    port = int(os.environ.get('PORT',8000))
    server_address = ('', port)
    httpd = ThreadHTTPServer(server_address, EmailResponder)
    httpd.serve_forever()
















# # compose an email message with body using the email native python library
# #some string that will become the body of the message
# body = 'Hello this is {} from mail-server.py'


# # set information for the body and the headers
# fromAddress = 'a.service.signup@gmail.com' 
# toAddress = 'eisen.dan@gmail.com'
# person = "Devon"

# # set the body of the message and instanciate the email messsage to be sent 
# email_message = MIMEText(body.format(person))


# #set the headers for the email incuding from and to
# email_message['Subject'] = "This is a message from {}{}".format(fromAddress, person)
# email_message['From'] = fromAddress
# email_message['To'] = toAddress

# #manage a connection to a mail server then send the email - finally time to use smtplib
# server_usernamae = 'a.service.signup@gmail.com'
# server_password = ''




# try:
#     email_server = smtplib.SMTP('smtp.gmail.com', 587)
#     email_server.starttls()
#     email_server.login(server_usernamae, server_password)
#     email_server.send_message(email_message)
#     email_server.quit()
# except smtplib.SMTPException:
#     print('We got some error! If you want to pin point it docs are here: https://docs.python.org/3.6/library/smtplib.html ')







# ref:
# https://docs.python.org/3.4/library/email-examples.html
# https://myaccount.google.com/u/1/lesssecureapps?pageId=none
# http://naelshiab.com/tutorial-send-email-python/
# https://support.google.com/a/answer/176600?hl=en

# define an smtp client session
# https://docs.python.org/3.6/library/smtplib.html

# run a python mail server
# https://docs.python.org/3.6/library/smtpd.html

# use mutipart form data
# http://nullege.com/codes/search/cgi.parse_multipart
# some of the methods of  cgi inherit from here
# https://docs.python.org/3/library/email.compat32-message.html#email.message.Message