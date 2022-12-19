from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os
import requests

# Base URL
url = 'https://www.googleapis.com/books/v1/volumes'

# API Key
load_dotenv()
api_key = os.environ['api_key']

def books_search():
    query = input("Enter search term for 5 books: ")
    params = {
        "q": query,
        "key": api_key,
        "max_results": '5'
    }

    response = requests.get(url, params=params)
    books = response.json()['items']

    for book in books:
        author = book['volumeInfo']['authors'][0]
        title = book['volumeInfo']['title']
        publisher = book['volumeInfo']['publisher']


books_search()