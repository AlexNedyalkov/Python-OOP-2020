"""
Class Gym
Upon initialization the class will not receive any parameters.
However, it should have the following attributes:
customers (list of customer objects, empty upon initialization),
trainers (list of trainer objects, empty upon initialization),
equipment (list of equipment objects, empty upon initialization),
plans (list of plan objects, empty upon initialization),
subscriptions (list of subscription objects, empty upon initialization)
Create the following methods:
•  add_customer(customer: Customer) – add the customer in the customer list, if the customer is not already in it
•  add_trainer(trainer: Trainer) – add the trainer to the trainers list, if the trainer is not already in it
•  add_equipment(equipment: Equipment) – add the equipment to the equipment list, if the equipment is not already in it
•  add_plan(plan: ExercisePlan) – add the plan to the plans list, if the plan is not already in it
•  add_subscription(subscription: Subscription) – add the subscription to the list, if not already in it
•  subscription_info(subscription_id:int) –
get the subscription, the customer and trainer to it, the plan to that trainer and the equipment to the plan.
Then return their string representations each separated by a new line

"""

class Gym:

    def __init__(self):
        self.customers: list = []
        self.trainers: list = []
        self.equipment: list = []
        self.plans: list = []
        self.subscriptions: list = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def subscription_info(self, subscription_id: int):
        subscription = list(filter(lambda s: s.id == subscription_id, self.subscriptions))[0]
        trainer = list(filter(lambda t: t.id == subscription.trainer_id, self.trainers))[0]
        customer = list(filter(lambda c: c.id == subscription.customer_id, self.customers))[0]
        plan = list(filter(lambda p: p.trainer_id == trainer.id, self.plans))[0]
        equipment = list(filter(lambda eq: eq.id == plan.equipment_id, self.equipment))[0]
        return subscription.__repr__() + '\n' + customer.__repr__() + '\n' + trainer.__repr__() + '\n' \
               + equipment.__repr__() + '\n' + plan.__repr__()


# from attributes_and_methods_03.exercises.gym_04.project.customer import Customer
# from attributes_and_methods_03.exercises.gym_04.project.equipment import Equipment
# from attributes_and_methods_03.exercises.gym_04.project.exercise_plan import ExercisePlan
# #from project.gym import Gym
# from attributes_and_methods_03.exercises.gym_04.project.subscription import Subscription
# from attributes_and_methods_03.exercises.gym_04.project.trainer import Trainer
#
# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
#
#
# """
# Subscription <1> on 14.05.2020
# Customer <1> John; Address: Maple Street; Email: john.smith@gmail.com
# Trainer <1> Peter
# Equipment <1> Treadmill
# Plan <1> with duration 20 minutes
# """