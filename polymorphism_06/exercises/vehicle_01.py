'''
Create an abstract class called Vehicle that should have abstract methods drive and refuel.
Create 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them.
Car and Truck both have fuel_quantity, fuel_consumption in liters per km and can be driven a given distance:
drive(distance) and refueled with a given amount of fuel: refuel(fuel).
 It is summer, so both vehicles use air conditioners and their fuel consumption per km when driving is increased by 0.9
 liters for the car and with 1.6 liters for the truck. Also, the Truck has a tiny hole in its tank and
 when it's refueled it keeps only 95% of the given fuel. The car has no problems and adds all the given fuel to its tank.
  If a vehicle cannot travel the given distance, its fuel does not change.
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
            self.fuel_quantity = fuel_quantity
            self.fuel_consumption = fuel_consumption
            self.fuel_consumption_increase = 0.9

    def drive(self, distance):
        quantity_needed = distance * (self.fuel_consumption + self.fuel_consumption_increase)
        if self.fuel_quantity >= quantity_needed:
            self.fuel_quantity -= (quantity_needed)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.fuel_consumption_increase = 1.6
        self.hole_refuel_damage = 0.05

    def drive(self, distance):
        quantity_needed = distance * (self.fuel_consumption + self.fuel_consumption_increase)
        if self.fuel_quantity >= quantity_needed:
            self.fuel_quantity -= (quantity_needed)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * (1 - self.hole_refuel_damage)

# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)