from project.vehicle.vehicle import Vehicle

"""
The Plane class should have the following attributes:
    • available_seats – int
    • rows – int
    • seats_per_row – int
    • seats_available – empty dict

The class should have method buy_tickets(row_number, tickets_count):
    • check if the given row number is valid and return the following message if it's not:
    "There is no row {row_number} in the plane!"
    • check if you can sell the given tickets count in the desired row using the method get_capacity from CapacityMixin
    and return tickets_count if the number of tickets is available for sale in this row.
    Don't forget to update the seats_available dictionary after selling some tickets!
    • If the number of tickets for the row number are not enough (smaller than the tickets_count)
    return the following message: "Not enough tickets on row {row_number}!"
"""
class Plane(Vehicle):

    def __init__(self, available_seats: int, rows: int, seats_per_row: int):
        super().__init__(available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}


    def buy_tickets(self, row_number, tickets_count):
        if row_number not in range(1, self.rows + 1):
            return f"There is no row {row_number} in the plane!"
        try:
            seats = self.seats_available[row_number] if row_number in self.seats_available else self.seats_per_row
            self.get_capacity(self.seats_available[row_number], tickets_count)
            self.seats_available[row_number] = self.seats_per_row - tickets_count
            self.available_seats -= tickets_count

        except Exception as ex:
            return str(ex)
p = Plane(20,4, 5)
print(p.buy_tickets(5, 10))
print(p.buy_tickets(4, 6))
print(p.buy_tickets(4, 4))
print(p.seats_available)
print(p.available_seats)