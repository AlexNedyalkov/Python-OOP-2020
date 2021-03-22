"""
Upon initialization each customer will receive the following parameters:
 name: str, address: str, email: str. Each customer should also have an id (autoincremented starting from 1)
Implement the __repr__ method so it returns the info about the customer in the following format:
"Customer <{id}> {name}; Address: {address}; Email: {email}"
Create a static method called get_next_id which returns the id that will be given to the next customer
"""
class Customer:

    autoincremental_id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.autoincremental_id
        Customer.autoincremental_id += 1

    @staticmethod
    def get_next_id():
        return Customer.autoincremental_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"