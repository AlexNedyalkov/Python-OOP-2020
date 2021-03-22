"""
Class Equipment
Upon initialization the class will receive the following parameters: name: str.
Each equipment should also have an id (autoincremented starting from 1)
Implement the __repr__ method so it returns the info about the equipment in the following format:
"Equipment <{id}> {name}"
Create a static method called get_next_id which returns the id that will be given to the next equipment
"""
class Equipment:

    autoincremental_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.autoincremental_id
        Equipment.autoincremental_id += 1

    @staticmethod
    def get_next_id():
        return Equipment.autoincremental_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

