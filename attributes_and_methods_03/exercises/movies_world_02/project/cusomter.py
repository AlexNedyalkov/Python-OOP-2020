"""
The Customer class should receive the following parameters upon initialization: name: str, age: int, id: int.
Each customer should also have an attribute called rented_dvds (list with DVD instances; empty upon initialization).
Implement the __repr__ method, so it returns the following string:
"{id}: {name} of age {age} has {count_rented_dvds} rented DVD's ({dvd_names joined by comma and space})"
"""
class Customer:

    def __init__(self, name: str, age: int, id: int):
        self.name: str = name
        self.age: int = age
        self.id: int = id
        self.rented_dvds: list = []

    def __repr__(self):
        rented_dvd_names = ", ".join([dvd.name for dvd in self.rented_dvds])
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)}" \
               f" rented DVD's ({rented_dvd_names})"

