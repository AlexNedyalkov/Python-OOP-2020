"""
    1. Smartphone
Create a class called Smartphone. Upon initialization it should receive a memory (number).
It should also have 2 other attributes: apps (empty list by default) and is_on (False by default). Create 3 methods:
    • power() - sets is_on on True if the phone is off, otherwise sets it to False
    • install(app, app_memory)
        ◦ If there is enough memory on the phone and it is on, install the app (add it to apps and decrease the memory of the phone) and return "Installing {app}"
        ◦ If there is enough memory, but the phone is off, return "Turn on your phone to install {app}"
        ◦ Otherwise return "Not enough memory to install {app}"
    • status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"

"""

class Smartphone:
    apps: list = []
    is_on: bool = False

    def __init__(self, memory: int):
        self.memory = memory

    def power(self):
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int):
        if self.memory - app_memory <= 0:
            return f"Not enough memory to install {app}"
        if not self.is_on:
            return f"Turn on your phone to install {app}"
        self.apps.append(app)
        self.memory -= app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


