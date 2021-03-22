#from collections import defaultdict
'''
    7. Library
Create class called Library, where the information regarding the users and books rented/available will be stored.
Create another one called User, where the information for each of the library users will be stored: user id, username and file with records of the books
rented by the current user.
Class Library
Upon initialization you won't receive anything. The class should have the following attributes:
    • user_records – empty list which will store the users (users objects) of the library
    • books_available – empty dictionary which will keep information regarding the authors (keys) and the books available for each of the authors (list)
    • rented_books – empty dictionary with usernames for keys and another dictionary as value in which the book names will be the keys
    and days to return the value ({usernames: {book names: days left}}).
You should also create 3 instance methods:
    • add_user(user: User):
        ◦ add the user if we do not have him/her in the library records already,
         otherwise return the message "User with id = {user_id} already registered in the library!"

    • remove_user(user: User):
        ◦ remove the user from the library records if available, otherwise return the message "We could not find such user to remove!"

    • change_username(user_id: int, new_username: str):
        ◦ change the username with the new provided and return the message "Username successfully changed to: {new_username} for userid: {user_id}"
        if there is a  record with the same user id in the library and the username is different than the provided one.
        ◦ If the username is the same for this id return the following message
        "Please check again the provided username - it should be different than the username used so far!".
        ◦ If there is no record for the provided id return "There is no user with id = {user_id}!"
'''
# from user import User

class Library:

    def __init__(self):
        self.user_records: list = []  # empty list which will store the users (users objects) of the library
        self.books_available: dict = {}
        self.rented_books: dict = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        users_after_filter = list(filter(lambda x: x.user_id == user_id, self.user_records))
        if len(users_after_filter) == 0:
            return f"There is no user with id = {user_id}!"
        elif users_after_filter[0].username == new_username:
            return f"Please check again the provided username -" \
                   f" it should be different than the username used so far!"
        else:
            users_after_filter[0].username = new_username
            return f"Username successfully changed to: {new_username} for userid: {user_id}"


#
# user = User(12, 'Peter')
# library = Library()
# library.add_user(user)
# print(library.add_user(user))
# library.remove_user(user)
# print(library.remove_user(user))
# library.add_user(user)
# print(library.change_username(2, 'Igor'))
# print(library.change_username(12, 'Peter'))
# print(library.change_username(12, 'George'))
#
# [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
#
#
# user.get_book('J.K.Rowling', 'The Deathly Hallows', 17, library)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
# print(user.get_book('J.K.Rowling', 'The Deathly Hallows', 10, library))
# print(user.return_book('J.K.Rowling', 'The Cursed Child', library))
# user.return_book('J.K.Rowling', 'The Deathly Hallows', library)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
