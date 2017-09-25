# Accra hottest event registration program
import sys
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import __init__

email = os.environ['GMAIL']
password = os.environ['PASSWORD']

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

contact_details = {}


def search_name(name_to_search):
    if name_to_search in contact_details.keys():
        print(contact_details[name_to_search])
    else:
        print('Contact was not found')


while True:
    print('Enter 1 to add contact  2 to search 3 to send email for email or q to exit')
    user_input = input()
    if user_input == '1':
        name = input('Please enter your name: ')
        email = input('Please enter your email address: ')
        contact_details[name] = email
        print(contact_details)
    if user_input == '2':
        name_to_be_searched = input('Please enter name to search: ')
        search_name(name_to_be_searched)
    if user_input == '3':
        person_to_send_email = input('Enter name of person to send email: ')
        if person_to_send_email in contact_details.keys():
            try:
                # Create message container - the correct MIME type is multipart/alternative.
                my_message = MIMEMultipart('alternative')
                my_message['Subject'] = "Accra is Proud of You!"
                my_message['From'] = 'Derrick Mwiti'
                my_message['To'] = contact_details[person_to_send_email]
                body = """
                        <html>
                      <head></head>
                      <body>
                        <p>Hi {} <b>This message is sent from Python</b>"!<br>
                           How are you?<br>
                           Here is the <a href="http://www.python.org">link</a> you wanted.
                        </p>
                      </body>
</html>
                       """.format(contact_details[person_to_send_email])
                body = MIMEText(body, 'html')
                my_message.attach(body)
                print('sending message to {}...'.format(contact_details[person_to_send_email]))
                server.sendmail(email, contact_details[person_to_send_email], my_message.as_string())
                print('Your email to {} is on the way..'.format(contact_details[person_to_send_email]))
                server.quit()
            except Exception as e:
                print('Sending failed', e)
        else:
            print('{} was not found in our contact list. Let\'s try this again...'.format(person_to_send_email))

    if user_input == 'q':
        print(contact_details)
        sys.exit()
