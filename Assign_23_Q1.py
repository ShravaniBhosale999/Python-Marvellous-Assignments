
class Bookstore:
    NoOfBooks =0
    def __init__(self, name, author):
        self.name = name
        self.author = author

        Bookstore.NoOfBooks += 1

    def display(self):
        print(f"{self.name} by {self.author}. No of books: {Bookstore.NoOfBooks}")

        # Creating objects

# Example usage
Obj1 = Bookstore("Linux System Programming", "Robert Love")
Obj1.display()

Obj2 = Bookstore("Python Crash Course", "Eric Matthes")
Obj2.display()