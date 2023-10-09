import csv

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Genre"])
            for book in self.books:
                writer.writerow([book.title, book.author, book.genre])

    def load_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                book = Book(row[0], row[1], row[2])
                self.books.append(book)