from list_functions import *

def display_books():
    selection = get_books()

    for i, book in enumerate(selection, start=1):
        author = book['author']
        title = book['title']
        publisher = book['publisher']
        
        print(f'{i}. Author: {author} || Title: {title} || Publisher: {publisher}')

    return ''

def book_interface():
    while True:
        mode = input(str(display_books()) + "\nSave 1 book.\n >> ")

        if mode == '1':
            return False

        elif mode == '2':
            pass

        if mode == '3':
            pass

        elif mode == '4':
            pass

        elif mode == '5':
            break