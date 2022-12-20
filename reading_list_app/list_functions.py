from dotenv import load_dotenv
import os
import requests

# Base URL
url = 'https://www.googleapis.com/books/v1/volumes'

# API Key
load_dotenv()
api_key = os.environ['api_key']

def get_books():
    query = input("Enter search term for 5 books: \n\n >> ")
    params = {
        "q": query,
        "filter": "full",
        "key": api_key,
        "max_results": '5'

    }

    response = requests.get(url, params=params)
    books = response.json()['items']
    selection = []

    for book in books:
        try:
            author = book['volumeInfo']['authors'][0]
        except: 
            author = "Data does not exist"

        try:
            title = book['volumeInfo']['title']
        except: 
            title = "Data does not exist"

        try:
            publisher = book['volumeInfo']['publisher']
        except: 
            publisher = "Data does not exist"

        selection.append({"author":author, "title": title, "publisher": publisher})

    return selection
