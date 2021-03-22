from project.vehicle.vehicle import Vehicle

"""
The Bus class should have the following attributes:
    • available_seats – int
    • ticket_price – float
    • tickets_sold = 0 at the beginning
The class should have the following methods:
    • get_ticket(tickets_count) – use method get_capacity from CapacityMixin to check if there are still seats available
     in the bus and track the current number of tickets sold.
    • get_total_profit() – return the profit from the sold tickets
"""
class Bus(Vehicle):

    def __init__(self, available_seats: int, ticket_price: float):
        super().__init__(available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = 0

    def get_ticket(self, tickets_count):
        try:
            self.get_capacity(self.available_seats, tickets_count)
            self.tickets_sold += tickets_count
            self.available_seats -= tickets_count
        except Exception as ex:
            return str(ex)

    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price


