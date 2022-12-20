from book_search_interface import book_interface

while True: 
    mode = input("\n== Reading List ==\n1. Search Books\n2. Reading List\n3. Exit\n\n>> ")

    if mode == '1':
        book_interface()

    elif mode == '2':
        pass

    elif mode == '3':
        break