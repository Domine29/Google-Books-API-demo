from book_search_interface import display_books

def saved_list_interface(saved_list):
    print("\n== Saved List ==\n")
    display_books(saved_list)

    if not saved_list:
        print("Reading List Empty")
    
    return
