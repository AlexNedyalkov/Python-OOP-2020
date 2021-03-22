"""
Class Zoo
Attributes
Private attribute animal_capacity: number
Private attribute workers_capacity: number
Private attribute budget: number
Public attribute name: string
Public attribute animals: list (empty upon initialization)
Public attribute workers: list (empty upon initialization)
"""

"""
Methods
__init__(name, budget, animlal_capacity, workers_capacity) - set the attributes to the given ones
add_animal(animal, price)
    • If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals list,
     reduce the budget and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
    • If you have capacity, but no budget, return "Not enough budget"
    • In any other case, you don't have space and you should return "Not enough space for animal"
hire_worker(worker)
    • If you have enough space for the worker (instance of Keeper/Caretaker/Vet), add him to the workers and
     return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
    • Otherwise return "Not enough space for worker"
fire_worker(worker_name)
    • If there is a worker with that name in the workers list, remove him and return "{worker_name} fired successfully"
    • Otherwise return "There is no {worker_name} in the zoo"
"""
from encapsulation_04.exercises.wild_cat_zoo.project.tiger import  Tiger
class Zoo:

    def __init__(self, name: str, budget:int, animal_capacity: int, workers_capacity: int):
        self.__animal_capacity: int = animal_capacity
        self.__workers_capacity: int = workers_capacity
        self.__budget: int = budget
        self.name: str = name
        self.animals: list = []
        self.workers: list = []

    # @property
    # def animal_capacity(self):
    #     return self.__animal_capacity
    #
    # @animal_capacity.setter
    # def animal_capacity(self, new_capacity):
    #     self.__animal_capacity = new_capacity
    #
    # @property
    # def workers_capacity(self):
    #     return self.__workers_capacity
    #
    # @workers_capacity.setter
    # def workers_capacity(self, new_capacity):
    #     self.__workers_capacity = new_capacity
    #
    # @property
    # def budget(self):
    #     return  self.__budget
    # @budget.setter
    # def budget(self, new_budget):
    #     self.__budget = new_budget


    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        elif len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget > total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_needs = sum([animal.get_needs() for animal in self.animals])
        if self.__budget > total_animal_needs:
            self.__budget -= total_animal_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message_to_return = f"You have {len(self.animals)} animals\n"
        lions = [animal for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = [animal for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        message_lion = f"----- {len(lions)} Lions:\n"
        for animal in lions:
            message_lion += f"Name: {animal.name}, Age: {animal.age}, Gender: {animal.gender}\n"
        message_tiger = f"----- {len(tigers)} Tiger:\n"
        for animal in tigers:
            message_tiger += f"Name: {animal.name}, Age: {animal.age}, Gender: {animal.gender}\n"
        message_cheetah = f"----- {len(cheetahs)} Cheetahs:\n"
        for animal in cheetahs:
            message_cheetah += f"Name: {animal.name}, Age: {animal.age}, Gender: {animal.gender}\n"
        message_to_return += message_lion + message_tiger + message_cheetah
        return message_to_return

    def workers_status(self):
        message_to_return = f"You have {len(self.workers)} workers\n"
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        message_keeper = f"----- {len(keepers)} Keepers:\n"
        for worker in keepers:
            message_keeper += str(worker.__repr__()) + "\n"
        message_caretaker = f"----- {len(caretakers)} Caretakers:\n"
        for worker in caretakers:
            message_caretaker += str(worker.__repr__()) + "\n"
        message_vets = f"----- {len(vets)} Vets:\n"
        for worker in vets:
            message_vets += str(worker.__repr__()) + "\n"
        message_to_return += message_keeper + message_caretaker + message_vets

        return message_to_return

from encapsulation_04.exercises.wild_cat_zoo.project.tiger import Tiger
from encapsulation_04.exercises.wild_cat_zoo.project.cheetah import Cheetah
from encapsulation_04.exercises.wild_cat_zoo.project.lion import Lion
from encapsulation_04.exercises.wild_cat_zoo.project.vet import Vet
from encapsulation_04.exercises.wild_cat_zoo.project.caretaker import Caretaker
from encapsulation_04.exercises.wild_cat_zoo.project.keeper import Keeper

# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Firing worker
# print(zoo.fire_worker("Sashko"))
#
# # Increase budget
# zoo.profit(100)
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
"""
workers_status()
    • Returns the following string:
You have {total_workers_count} workers
----- {amount_of_keepers} Keepers:
{keeper1}
…
----- {amount_of_caretakers} Caretakers:
{caretaker1}
…
----- {amount_of_vetes} Vets:
{vet1}
…
    • Hint: use the __repr__ methods of the workers to print them on the console
"""




