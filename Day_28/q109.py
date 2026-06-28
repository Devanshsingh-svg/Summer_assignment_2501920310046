class Library:
    def __init__(self):
        self.books = set()
    def add_book(self, book: str):
        self.books.add(book)
    def issue_book(self, book: str):
        if book in self.books:
            self.books.remove(book)
            return True
        return False

if __name__ == "__main__":
    lib = Library()
    lib.add_book("1984")
    print("Issued 1984:", lib.issue_book("1984"))
