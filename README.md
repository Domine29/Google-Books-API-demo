# Google-Books-API-demo
  - The Command Line Interface (CLI) will have three options displayed...
    - Search
      - User inputs search query then Google Books API retrieves 5 books matching query and displays it to the user
      - User selects a book from the list and saves it to the "Reading List"
    - Reading List
      - User will be able to see a list of books they have saved. 
    - Exit

## Approach
  - Render the main app interface containing...
    - Search interface
      1. Search will use request.get() to fetch data from the endpoint. Which then gets displayed on the command line.
      2. User can then select which one they want to save.
    - Saved List interface
      1. A user's saved books get displayed to view on the command line.
  
## Set Up
1. Create Virtual Environment ([Documentation](https://docs.python.org/3/library/venv.html))
    - In parent folder, in the command line of your terminal run ``` python3 -m venv <my-env> ```
    - In the same level as your virtual environment, run ``` source <my-env>/bin/activate ``` to activate your virtual environment. 
    - To deactivate run ``` deactivate ```
2. Install dependencies using pip
    - Ensure you have pip installed ([Documentation](https://pip.pypa.io/en/stable/installation/))
    - A "requirements.txt" is included in the repo to ensure your virtual environment has all the necessary dependencies to run the application. 
    - In the same level as "requirements.txt" run ``` pip install -r requirements.txt ```
3. Using an optional API Key
    - The application is setup to not use an API key, but some might find that the Google Books API might be limited in functionality and prefer to use an API key.
    - Acquire an API key from the Google Books API. The [Documentation](https://developers.google.com/books/docs/v1/using#OAuth2Authorizing) for the API provides steps to get an API key and also includes how to use the API if you wish to customize the application further. 
    - Create a .env file in the parent folder and in the file create a variable called "api_key" and set it equal to your API key. 
    - If you do not want to share your API key with other users then create a ".gitingnore" file and include the ".env" in the ".gitignore". Anything included in the ".gitignore" will not be pushed up into your repo. 
    - In the "reading_list_app" folder, the "list_functions.py" contains all functionality for the Google Books API. Uncomment line 16 of the code which includes the "key" parameter.
4. Run Application
    - Under "reading_list_app" folder run ``` python reading_list_interface.py ``` to interact with the application.
    
## Functionality
1. "reading_list_interface.py"
    - The main application that has two main functions kept in two separate files: The Search Functionality and The Saved List Functionality
2. The Search Functionality: "book_search_interface.py"
    - This interface asks the user to enter a search term and bundles it with other parameters in a get request to the Google Books API. That functionality lives under "list_functions.py". 
    - The get request returns a list of 5 objects representing books with author, title, and publisher information. This list is saved as a variable named selection. 
    - The "display_books(selection):" function takes those 5 books and displays them in the command line. The user is prompted to select one. 
    - The chosen option is then passed to the "select_book(book):" function. The json file under "data" folder is opened and the list is saved as a variable. The chosen option is then appended to the end of the variable. Finally, the json file is opened again and the updated variable overwrites the previous data in the json file. 
3. The Saved List Functionality: "saved_list_interface.py"
    - The main interface opens the json file and saves the data in a variable. The variable is passed to the "saved_list_interface(saved_list)" function.
    - The "display_books(saved_list):" function is reused here to display the saved books. 
    
