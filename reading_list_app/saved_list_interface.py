from book_search_interface import display_books

def saved_list_interface(saved_list):
    if not saved_list:
        print("No saved book(s)")
        return
    
    display_books(saved_list)
    
    return
