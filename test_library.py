import unittest
from library import Book, Library

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Title", "Author", "Genre")
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.genre, "Genre")


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
    
    def test_add_book(self):
        book = Book("Title", "Author", "Genre")
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)

    def test_display_books(self):
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        self.library.display_books()

        printed_output = sys.stdout.getvalue()
        sys.stdout = saved_stdout
        self.assertTrue("Title" in printed_output)
        self.assertTrue("Author" in printed_output)
        self.assertTrue("Genre" in printed_output)

if __name__ == '__main__':
    unittest.main()
