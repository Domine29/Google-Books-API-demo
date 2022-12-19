# Google-Books-API-demo

## Overall Structure
  - The Command Line Interface (CLI) will have three options displayed
    1. Search
      - User inputs search query then Google Books API retrieves 5 books matching query and displays it to the user
      - User selects a book from the list and saves it to the "Reading List"
    2. Reading List
      - User will be able to see a list of books they have saved. 

## Approach
  - Render interface
  - Search will use request.get() to fetch data from the endpoint
  - When a user picks one book, using OOP, creates an instance of the class "Book" then saves it to a global variable that is an array of objects that can be iterated through and displayed. 