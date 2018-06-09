#!/usr/bin/env python3

#import smtplib for sending the email ie. run an email server
import smtplib

#import any email modules needed to construct headers and format the email itself
from email.mime.text import MIMEText

# compose an email message with body using the email native python library
#some string that will become the body of the message
body = 'Hello this is {} from mail-server.py'


# set information for the body and the headers
fromAddress = 'a.service.signup@gmail.com' 
toAddress = 'eisen.dan@gmail.com'
person = "Devon"

# set the body of the message and instanciate the email messsage to be sent 
email_message = MIMEText(body.format(person))


#set the headers for the email incuding from and to
email_message['Subject'] = "This is a message from {}{}".format(fromAddress, person)
email_message['From'] = fromAddress
email_message['To'] = toAddress

#manage a connection to a mail server then send the email - finally time to use smtplib
server_usernamae = 'a.service.signup@gmail.com'
server_password = ';;;p;;;_Pearl_'




try:
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.starttls()
    email_server.login(server_usernamae, server_password)
    email_server.send_message(email_message)
    email_server.quit()
except smtplib.SMTPException:
    print('We got some error! If you want to pin point it docs are here: https://docs.python.org/3.6/library/smtplib.html ')







# ref:
# https://docs.python.org/3.4/library/email-examples.html
# https://myaccount.google.com/u/1/lesssecureapps?pageId=none
# http://naelshiab.com/tutorial-send-email-python/
# https://support.google.com/a/answer/176600?hl=en

# define an smtp client session
# https://docs.python.org/3.6/library/smtplib.html

# run a python mail server
# https://docs.python.org/3.6/library/smtpd.html