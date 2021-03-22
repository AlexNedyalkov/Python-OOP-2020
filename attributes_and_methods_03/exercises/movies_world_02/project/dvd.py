"""
The DVD class should receive the following parameters upon initialization:
 name: str, id: int, creation_year: int, creation_month: str, age_restriction: int.
 Each DVD should also have an attribute called is_rented (False by default)
Implement the __repr__ method so it returns the following string:
"{id}: {name} ({creation_month} {creation_year}) has age restriction {age_restriction}. Status: {rented/not rented}"
Create one more method called from_date(id: int, name: str, date: str, age_restriction: int) – it should create a new
instance using the provided data. The date will be in format "day.month.year" – all of them numbers.
"""
import datetime

class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name: str = name
        self.id: int = id
        self.creation_year: int = creation_year
        self.creation_month: str = creation_month
        self.age_restriction: int = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date_split = datetime.datetime.strptime(date, '%d.%m.%Y')
        return cls(name, id, date_split.date().year, date_split.strftime("%B"), age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"