from project.technology.technology import Technology
"""
The Laptop class should have the following attributes:
    • memory – float
    • memory_taken – float
The class should have method install_software(software, software_memory):
    • check if you have memory to install the software and return the memory left after the install if sucessfully,
    otherwise return "You don't have enough space for {software}!"

"""
class Laptop(Technology):

    def install_software(self, software, software_memory):
        if self.memory - software_memory < 0:
            return f"You don't have enough space for {software}!"
        return self.memory - software_memory

