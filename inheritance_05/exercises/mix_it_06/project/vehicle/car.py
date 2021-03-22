from project.vehicle.vehicle import Vehicle
"""
The Car class should have the following attributes:
    • available_seats – int
    • fuel_tank – int
    • fuel_consumption – float
    • fuel – float
Create getter and setter for attribute fuel and validate the fuel not to exceed the fuel capacity. 

The class should have the following methods:
    • drive(distance) – check if you have enough fuel to travel the given distance.
    Reduce the fuel if you've managed to drive the car and return the following message " We've enjoyed the travel!".
    
    • refuel(liters) – check if you have enough space in the tank to take the given liters.
    Increase the fuel in the tank and return the liters available or return "Capacity reached!". 
    To do this inherit CapacityMixin with method named get_capacity(capacity, amount) which will return the message 
    above if the amount provided is bigger than the capacity, 
    otherwise - the difference between the capacity and the given amount.
"""
class Car(Vehicle):

    def __init__(self, available_seats: int, fuel_tank: int, fuel_consumption: float, fuel: float):
        # Vehicle.__init__(self, available_seats)
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, new_fuel: float):
        if self.__fuel <= float(self.fuel_tank):
            self.__fuel = new_fuel
        else:
            self.__fuel = self.fuel_tank

    #TODO check if the return message should have _ before We
    def drive(self, distance):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        try:
            self.get_capacity(self.fuel_tank, liters + self.fuel)
            self.fuel += liters
            return self.fuel
        except Exception as ex:
            return str(ex)

# my_car = Car(4, 50, 3,20)
# print(my_car.drive(10))
# print(my_car.refuel(46))




