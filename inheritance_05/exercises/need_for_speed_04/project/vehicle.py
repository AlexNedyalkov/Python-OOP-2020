"""
Create a base class Vehicle. It should contain the following attributes:
    • DEFAULT_FUEL_CONSUMPTION – float (constant)
    • fuel_consumption – float
    • fuel – float
    • horse_power – int
    • A public constructor which accepts (fuel, horse_power)
    and set the default fuel consumption on the attribute fuel_consumption

The class should have the following methods:
    • drive(kilometers)
        ◦ The drive method should have a functionality to reduce the fuel based on the travelled kilometers
        and fuel consumption. Keep in mind that you can drive the vehicle only
        if you have enough fuel to finish the driving.
The default fuel consumption for Vehicle is 1.25. Some of the classes have different default fuel consumption:
    • SportCar – DEFAULT_FUEL_CONSUMPTION = 10
    • RaceMotorcycle – DEFAULT_FUEL_CONSUMPTION = 8
    • Car – DEFAULT_FUEL_CONSUMPTION = 3
"""
class Vehicle:

    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if self.fuel >= fuel_needed:
            self.fuel -= self.fuel_consumption * kilometers

