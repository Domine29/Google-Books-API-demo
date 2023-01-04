from book_search_interface import book_interface
import book_search_interface
from saved_list_interface import *

error_message = ''

while True: 
    mode = input(f"\n== Reading List ==\n1. Search Books\n2. Reading List\n3. Exit{error_message}\n\n>> ")

    if mode == '1':
        error_message = ''
        book_interface()

    elif mode == '2':
        error_message = ''
        saved_list_interface(book_search_interface.saved_list)

    elif mode == '3':
        break

    else:
        error_message = "\n\nPlease choose option 1,2 or 3."