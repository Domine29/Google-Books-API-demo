from book_search_interface import book_interface
from saved_list_interface import *
import json

error_message = ''

while True: 
    with open('./data/saved_list.json', 'r') as file:
        saved_list = json.load(file)

    mode = input(f"\n== Reading List ==\n1. Search Books\n2. Reading List\n3. Exit{error_message}\n\n>> ")

    if mode == '1':
        error_message = ''
        book_interface()

    elif mode == '2':
        error_message = ''
        saved_list_interface(saved_list)

    elif mode == '3':
        print('\nGoodbye\n')
        break

    else:
        error_message = "\n\nPlease choose option 1,2 or 3."