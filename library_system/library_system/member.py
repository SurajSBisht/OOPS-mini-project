class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.borrowed_count = 0

    def borrow_book(self, book):
        print("Generic borrow — use a specific member type.")

    def display(self):
        print(f"ID   : {self.member_id}")
        print(f"Name : {self.member_name}")
