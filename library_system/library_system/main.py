import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from book import Book
from student_member import StudentMember
from faculty_member import FacultyMember


def display_all_books(books):
    for book in books:
        book.display()


def main():
    print("=" * 30)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 25)

    book1 = Book(101, "Python Programming", "John Smith")
    book2 = Book(102, "Data Structures", "Alice Brown")
    book3 = Book(103, "Database Systems", "Robert King")
    books = [book1, book2, book3]

    student = StudentMember(1, "Rahul Sharma")
    faculty = FacultyMember(2, "Dr. Mehta")

    print("\nAvailable Books\n")
    display_all_books(books)

    print("\nMember Details\n")
    student.display()

    print()
    student.borrow_book(book1)
    print()
    student.borrow_book(book2)
    print()
    student.borrow_book(book3)

    print("\nBook Status\n")
    display_all_books(books)

    print("\nFaculty Member Details\n")
    faculty.display()

    print()
    faculty.borrow_book(book3)
    print()
    faculty.borrow_book(book1)

    print("\nFinal Book Status\n")
    display_all_books(books)

    print()
    faculty.display()


if __name__ == "__main__":
    main()
