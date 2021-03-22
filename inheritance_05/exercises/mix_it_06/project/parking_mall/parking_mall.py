from project.capacity_mixin import CapacityMixin
"""
Class ParkingMall will get parking_lots: int upon initialization. 
The class should have method check_availability():
    • using the get_capacity method from CapacityMixin class check if
     there are any slots available in the level and return "Parking lots available: {self.parking_lots} ".
      If there are no places available in this level return "There are no more parking lots!"

Classes Level1, Level2 and Level3 will inherit class ParkingMall. Level1 has 150 parking lots, 
Level2 has 100 parking lots and Level3 has 80 parking.
"""
class ParkingMall(CapacityMixin):

    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        try:
            self.check_availability(self.parking_lots, 1)
            self.parking_lots -= 1
            return f"Parking lots available: {self.parking_lots}"
        except Exception:
            return "There are no more parking lots!"