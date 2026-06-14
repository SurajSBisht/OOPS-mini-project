from member import Member

class StudentMember(Member):
    BORROW_LIMIT = 2

    def __init__(self, member_id, member_name):
        super().__init__(member_id, member_name)

    def borrow_book(self, book):
        print("Borrowing Book:")
        if self.borrowed_count >= self.BORROW_LIMIT:
            print("Borrowing limit reached.")
            return
        if not book.is_available():
            print(f"'{book.title}' is not available.")
            return
        book.set_available(False)
        self.borrowed_count += 1
        print(f"{book.title} borrowed successfully.")

    def display(self):
        super().display()
        print("Type : Student Member")
        print(f"Borrowed Books Count : {self.borrowed_count}")
