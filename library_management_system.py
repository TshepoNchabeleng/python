class Books:
    def __init__(self):
        pass
        self.books = {}

    def available_books(self):
        self.books = {
            "book1" : ("Harry Potter", "J.K Rowling", 1),
            "book2" : ("Atomic Habits", "James Clear", 2),
            "book3" : ("Pride and Prejudice", "Jane Austen", 3),
            "book4" : ("Jane Eyre", "Charlotte Bronte", 4),
            "book5" : ("Little Women", "Louisa May Alcott", 5),
            "book6" : ("Wuthering Heights", "Emily Bronte", 6)
        }
    
    def borrowed_books(self, book_key):
        for key in self.books :
            if key in book_key:
                removed_books = self.books.pop(key)
                print(f"Removed: {removed_books[key]} (Key: {key})")
            else:
                print(f"Error with book key '{key}' not found or already borrowed")

    def left_books(self):
        if not self.books:
            print("No books are currently available in the library")
            return
        for key, details in self.books.items():
            title = details[0]
            author = details[1]
            print(f"{key}: {title} by {author}")


books = Books()
books.borrowed_books(["book1", "book3"])
books.left_books()