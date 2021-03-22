from attributes_and_methods_03.exercises.movies_world_02.project.cusomter import Customer
from attributes_and_methods_03.exercises.movies_world_02.project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name: str = name
        self.customers: list = []
        self.dvds: list = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = list(filter(lambda c: (c.id == customer_id), self.customers))[0]
        dvd = list(filter(lambda d: (d.id == dvd_id), self.dvds))[0]
        rented_dvds = list(filter(lambda d: (d.is_rented == True), self.dvds))
        if dvd in rented_dvds:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return f"DVD is already rented"
        else:
            if customer.age < dvd.age_restriction:
               return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
            else:
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = list(filter(lambda c: (c.id == customer_id), self.customers))[0]
        dvd = list(filter(lambda d: (d.id == dvd_id), self.dvds))[0]
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        message_customers = ""
        message_dvds = ""
        count = 1
        for customer in self.customers:

            dvd_names = []

            for dvd in customer.rented_dvds:
                dvd_names.append(dvd.name)
                dvd_names_str = ", ".join(dvd_names)

            message_customers += str(f"{count}: {customer.name} of age {customer.age} has"
                               f" {len(customer.rented_dvds)} rented DVD's ({dvd_names_str})")
            message_customers += "\n"
            count += 1
        count = 1
        for dvd in self.dvds:
            if dvd.is_rented:
                status = "rented"
            else:
                status = "not rented"
            message_dvds += (str(f"{count}: {dvd.name} ({dvd.creation_month} {dvd.creation_year})"
                               f" has age restriction {dvd.age_restriction}. Status: {status}"))
            count += 1
            message_dvds += "\n"
        return message_customers + message_dvds

# from project.customer import Customer
# from project.dvd import DVD
# from project.movie_world import MovieWorld

c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)


"""
John should be at least 18 to rent this movie
Anna has successfully rented Black Widow
John has successfully rented The Croods 2
1: John of age 16 has 1 rented DVD's (The Croods 2)
2: Anna of age 55 has 1 rented DVD's (Black Widow)
1: Black Widow (April 2020) has age restriction 18. Status: rented
2: The Croods 2 (December 2020) has age restriction 3. Status: rented
"""