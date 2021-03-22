"""
    5. Time
Create a class called Time. Upon initialization it should receive hours, minutes and seconds (numbers).
The class should also have class attributes max_hours equal to 23, max_minutes equal to 59 and max_seconds equal to 59.
You should also create 3 instance methods:
    • set_time(hours, minutes, seconds) - update the time
    • get_time() - returns "{hh}:{mm}:{ss}"
    • next_second() - update the time with one second (use the class attributes for validation) and return the new time (using the get_time() method)
"""

class Time:

    max_hours: int = 23
    max_minutes: int = 59
    max_seconds: int = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        if self.hours == Time.max_hours and self.minutes == Time.max_minutes and self.seconds == Time.max_seconds:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif Time.max_minutes == self.minutes and Time.max_seconds == self.seconds:
            self.hours += 1
            self.minutes = 0
            self.seconds = 0
        elif Time.max_seconds == self.seconds:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1
        return self.get_time()


#
# time = Time(9, 30, 59)
# print(time.next_second())
# time = Time(10, 59, 59)
# print(time.next_second())
# time = Time(23, 59, 59)
# print(time.next_second())

"""
09:31:00
11:00:00
00:00:00

"""