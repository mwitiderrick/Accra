# Accra hottest e vent
import sys

contact_details = {}


def search_name(name_to_search):
    if name_to_search in contact_details.keys():
        print(contact_details[name_to_search])
    else:
        print('Contact was not found')


while True:
    print('Enter 1 to add contact  2 to search for email or q to exit')
    user_input = input()
    if user_input == '1':
        name = input('Please enter your name: ')
        email = input('Please enter your email address: ')
        contact_details[name] = email
    if user_input == '2':
        name_to_be_searched = input('Please enter name to search: ')
        search_name(name_to_be_searched)
    if user_input == 'q':
        print(contact_details)
        sys.exit()
