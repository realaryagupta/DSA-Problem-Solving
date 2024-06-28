class Books:
    def __init__(self):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
    
    def __str__(self):
        print(f"The name of Book is {self.title}. The name of author is {self.author}. ISBN Number of {self.title} is {self.isbn}. It has {self.copies} in Library")

    def borrow(self):
        if self.copies > 0:
            self.copies = self.copies - 1
            print("Book borrowed successfully.")
        else:
            print("Book Out of Stock Currently")

    def return_book(self):
        if self.copies > -1:
            self.copies = self.copies + 1
            return True
        else:
            print("Error")

    


class Members:
    def __init__(self) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {', '.join([book.title for book in self.borrowed_books])}"

    




        






