"""
    2. Vet
Create a class called Vet. Upon initialization it should receive a name (string).
It should also have an instance attribute called animals (empty list by default).
There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets;
space (5 by default). You have to create 3 more instance methods
    • register_animal(animal_name)
        ◦ If there is space in the vet clinic add the animal to both animals lists and return a message: "{name} registered in the clinic"
        ◦ Otherwise return "Not enough space"
    • unregister_animal(animal_name)
        ◦ If the animal is in the relevant vet list, remove it from both animals lists and return "{animal} unregistered successfully"
        ◦ Otherwise, return "{animal} not in the clinic"
    • info() - returns "{vet_name} has {amount_of_his_animals} animals. {space_left_in_clinic} space left in clinic"
"""
class Vet:

    animals: list = []
    space:int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str):
        if self.space > 0:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            Vet.space -= 1
            return f'{animal_name} registered in the clinic'
        return 'Not enough space'

    def unregister_animal(self, animal_name: str):
        if animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f'{animal_name} unregistered successfully'
        return f'{animal_name} not in the clinic'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic'

# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())
