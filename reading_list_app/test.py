import unittest
import mock
from list_functions import get_books
import json
from book_search_interface import select_book

class TestReadingInterface(unittest.TestCase):

    # def test_get(self):
    #     with mock.patch('requests.get') as mock_get:
    #         mock_get.return_value.json.return_value = {
    #             "totalItems": 1, 
    #             "items": [{
    #                 "volumeInfo": {
    #                     "author": ["Author"],
    #                     "title": "Title",
    #                     "publisher": "Publisher"
    #                 }
    #             }]
    #         }
    #         books = get_books()
    #         self.assertEqual(books, {"author": ["Author 1"], "title": "Title 1", "publisher": "Publisher 1"})

    def test_select_book(self):
        with open('./data/saved_list.json', 'r') as file:
            saved_list = json.load(file)
        
        select_book({"author": "Author", "title": "Title", "publisher": "Publisher"})

        with open('./data/saved_list.json', 'r') as file:
            updated_saved_list = json.load(file)

            self.assertEqual(len(updated_saved_list), len(saved_list) + 1)

            self.assertEqual(updated_saved_list[-1], {"author": "Author", "title": "Title", "publisher": "Publisher"})
        
        with open('./data/saved_list.json', 'w') as file:
            json.dump(saved_list, file)


if __name__ == '__main__':
    unittest.main()