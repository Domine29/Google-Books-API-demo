from list_functions import *

saved_list = []

def select_book(book):
    saved_list.append(book)

def display_books(selection):

    for i, book in enumerate(selection, start=1):
        author = book['author']
        title = book['title']
        publisher = book['publisher']
        
        print(f'{i}. Author: {author} || Title: {title} || Publisher: {publisher}')

    return ''

def book_interface():
    selection = get_books()

    while True:
        mode = input(str(display_books(selection)) + "6. Exit\n\nSave 1 book.\n\n >> ")

        if mode == '1':
            select_book(selection[0])
            return False

        elif mode == '2':
            select_book(selection[1])
            return False

        if mode == '3':
            select_book(selection[2])
            return False

        elif mode == '4':
            select_book(selection[3])
            return False

        elif mode == '5':
            select_book(selection[4])
            return False

        elif mode == '6':
            break