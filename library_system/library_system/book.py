class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__available = True

    def is_available(self):
        return self.__available

    def set_available(self, status):
        self.__available = status

    def display(self):
        status = "Available" if self.__available else "Not Available"
        print(f"{self.book_id} - {self.title} - {status}")
