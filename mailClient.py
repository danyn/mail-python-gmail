

def send(first_name, last_name, email_address, telephone_number):

    #import smtplib for sending the email ie. Connect as a client to a email server
    import smtplib

    #import any email modules needed to construct headers and format the email itself
    from email.mime.text import MIMEText

    # compose an email message with body using the email native python library
    #some string that will become the body of the message
    body = '''You have an email from {}.

    The email address to reply to is:{}
    The Telephone number to reply to is:{} 
    
    '''
    # set information for the body and the headers
   
    toAddress = 'eisen.dan@gmail.com'
    person = first_name + ' ' + last_name

    # set the body of the message and instanciate the email messsage to be sent 
    email_message = MIMEText(body.format(person, email_address, telephone_number))


    #set the headers for the email incuding from and to
    email_message['Subject'] = "This is a message from {} sent by {}".format(email_address, person)
    email_message['From'] = email_address
    email_message['To'] = toAddress

    #manage a connection to a mail server then send the email - finally time to use smtplib
    server_usernamae = 'a.service.signup@gmail.com'
    server_password = ''




    try:
        email_server = smtplib.SMTP('smtp.gmail.com', 587)
        email_server.starttls()
        email_server.login(server_usernamae, server_password)
        email_server.send_message(email_message)
        email_server.quit()
    except smtplib.SMTPException:
        print('We got some error! If you want to pin point it docs are here: https://docs.python.org/3.6/library/smtplib.html ')
