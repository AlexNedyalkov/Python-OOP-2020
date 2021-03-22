"""
Class Technology will get memory: float and memory_taken: float upon initialization.
Classes Laptop and SmarhPhone will inherit class Technology.
"""
class Technology:

    def __init__(self, memory,  memory_taken):
        self.memory = memory
        self.memory_taken = memory_taken