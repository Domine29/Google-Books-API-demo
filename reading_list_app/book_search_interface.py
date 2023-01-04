from list_functions import *
import json

def select_book(book):
    with open('./data/saved_list.json', 'r') as file:
        saved_list = json.load(file)
    
    saved_list.append(book)

    with open('./data/saved_list.json', 'w') as file:
        json.dump(saved_list, file)

def display_books(selection):

    for i, book in enumerate(selection, start=1):
        author = ", ".join(book['author']) if isinstance(book['author'], list) else book['author']

        title = book['title']
        publisher = book['publisher']
        
        print(f'{i}. Author(s): {author} || Title: {title} || Publisher: {publisher}')

    return ''

def book_interface():

    selection = get_books()
    error_message = ''

    while True:

        if not selection:
            error_message = "\n\nInvalid search term or book does not exist, please try again\n"

            print(error_message)

            error_message = ''
            selection = get_books()

            continue

        mode = input(str(display_books(selection)) + f"6. Go Back{error_message}\n\nSave 1 book.\n\n >> ")

        if mode == '1':
            select_book(selection[0])
            print(f"\n{selection[0]['title']} has been saved ")
            return False

        elif mode == '2':
            select_book(selection[1])
            print(f"\n{selection[1]['title']} has been saved ")
            return False

        if mode == '3':
            select_book(selection[2])
            print(f"\n{selection[2]['title']} has been saved ")
            return False

        elif mode == '4':
            select_book(selection[3])
            print(f"\n{selection[3]['title']} has been saved ")
            return False

        elif mode == '5':
            select_book(selection[4])
            print(f"\n{selection[4]['title']} has been saved ")
            return False

        elif mode == '6':
            break
        
        else:
            error_message = "\n\nPlease choose one Book from 1-5 or 6 to go back"