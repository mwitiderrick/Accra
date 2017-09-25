# Accra hottest event registration program
import sys
import smtplib
from config import password, email  # Pick the variables from config.py not in
#  project because it has my email and password

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
                my_message = "Hi {} This message is sent from Python".format(contact_details[person_to_send_email])
                print('sending message to {}...'.format(contact_details[person_to_send_email]))
                server.sendmail(email, contact_details[person_to_send_email], my_message)
                server.quit()
            except Exception as e:
                print('Sending failed', e)
        else:
            print('{} was not found in our contact list. Let\'s try this again...'.format(person_to_send_email))

    if user_input == 'q':
        print(contact_details)
        sys.exit()
