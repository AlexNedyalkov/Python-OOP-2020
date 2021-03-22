from project.technology.technology import Technology

"""
The SmartPhone class should have the following attributes:
    • memory – float
    • memory_taken – float
The class should have method install_apps(app, app_memory):
    • check if you have memory to install the app and return the memory left after the install if sucessfully,
     otherwise return "You don't have enough space for {app}!"
"""
class SmartPhone(Technology):

    def install_app(self, app, app_memory):
        if self.memory - app_memory < 0:
            return f"You don't have enough space for {app}!"
        return self.memory - app_memory