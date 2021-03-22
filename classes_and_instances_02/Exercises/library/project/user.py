"""
Class User
Upon initialization it should receive user_id(int) and username(string).
The class should also have an attribute books which will be an empty list at the beginning. You should also create 3 instance methods:
    • get_book(author: str, book_name: str, days_to_return: int, library: Library):
        ◦ if the book is available in the library add it to the books list for this user,
        update the library records (rented_books and available_books dicts)
        and return the following message: "{book_name} successfully rented for the next {days_to_return} days!"
        ◦ if it's already rented return the following message
        "The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!"

    • return_book(author:str, book_name:str, library: Library):
        ◦ if the book is in the user's books list return it in the library (update books_available and rented_books class attributes)
        and remove it from the books list for this user
        ◦ otherwise return the following message "{username} doesn't have this book in his/her records!"

    • info() – return a string containing the books currently rented by the user in ascending order separated by comma and space.
    • You should also override the __string__ method in order to get a string in the following format "{user_id}, {username}, {books}"
"""
#from Exercises.library.project.library import Library

class User:



    def __init__(self, user_id: int, username: str):
        self.books: list = []
        self.user_id: int = user_id
        self.username: str = username

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books.keys():
                library.rented_books[self.username] = {}
            library.rented_books[self.username].update({book_name: days_to_return})
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, data in library.rented_books.items():
            for b_n, days in data.items():
                if b_n == book_name:
                    return f"The book \"{book_name}\" " \
                           f"is already rented and will be available in " \
                           f"{days} days!"
    def return_book(self, author:str, book_name:str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        library.rented_books[self.username].pop(book_name)
        library.books_available[author].append(book_name)
        self.books.remove(book_name)

    def info(self):
        return f"{', '.join(sorted(self.books))}"


    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
