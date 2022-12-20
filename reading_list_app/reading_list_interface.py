from book_search_interface import book_interface
import book_search_interface
from saved_list_interface import *

while True: 
    mode = input("\n== Reading List ==\n1. Search Books\n2. Reading List\n3. Exit\n\n>> ")

    if mode == '1':
        book_interface()

    elif mode == '2':
        saved_list_interface(book_search_interface.saved_list)

    elif mode == '3':
        break