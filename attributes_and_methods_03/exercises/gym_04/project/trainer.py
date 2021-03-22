"""
Class Trainer
Upon initialization the class will receive the following parameters: name:str.
The class should also have an id (autoincremented starting from 1).
Implement the __repr__ method so it returns the info about the trainer in the following format:
"Trainer <{self.id}> {self.name}"
Create a static method called get_next_id which returns the id that will be given to the next trainer
"""
class Trainer:

    autoincremental_id = 1

    def __init__(self, name: str):
        self.name: str = name
        self.id = Trainer.autoincremental_id
        Trainer.autoincremental_id += 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.autoincremental_id