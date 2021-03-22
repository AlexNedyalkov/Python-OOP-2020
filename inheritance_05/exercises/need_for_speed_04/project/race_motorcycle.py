from project.motorcycle import Motorcycle

class RaceMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION = 8


my_race_motorcycle = RaceMotorcycle(10, 5)
print(my_race_motorcycle.fuel)
my_race_motorcycle.drive(1)
print(my_race_motorcycle.fuel)