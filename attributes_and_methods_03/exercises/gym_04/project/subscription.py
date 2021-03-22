"""
Class Subscription
Upon initialization the class will receive the following parameters:
date:str, customer_id: int, trainer_id: int, exercise_id: int.
The class should also have an id (autoincremented starting from 1).
Implement the __repr__ method so it returns the info about the subscription in the following format: "Subscription <{id}> on {date}"
Create a static method called get_next_id which returns the id that will be given to the next subscription
"""

class Subscription:

    autoincremetal_id = 1

    def __init__(self, date:str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date: str = date
        self.customer_id: int = customer_id
        self.trainer_id: int = trainer_id
        self.exercise_id: int = exercise_id
        self.id = Subscription.autoincremetal_id
        Subscription.autoincremetal_id += 1

    @staticmethod
    def get_next_id():
        return Subscription.autoincremetal_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"