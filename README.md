# Google-Books-API-demo

## Overall Structure
  - The Command Line Interface (CLI) will have three options displayed
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
  - <strike>When a user picks one book, using OOP, creates an instance of the class "Book" then saves it to a global variable that is an array of objects that can be iterated through and displayed.<strike>
