class Father:

    def __init__(self, name):
        self.father_name = name


class Mother:

    def __init__(self, name):
        self.mother_name = name

class Daughter(Father, Mother):

    def __init__(self, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

    def get_parent_info(self):
        return f"Father: {self.father_name}, Mother: {self.mother_name}"

child = Daughter("Taylor Evans", "Bet Williams")
print(child.get_parent_info())

class Base:
   def __init__(self, name):
      self.name = name

   def get_name(self):
      return self.name

class Child(Base):
   def __init__(self, name, age):
      super().__init__(name)
      self.age = age

   def get_age(self):
      return self.age

class GrandChild(Child):

    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def return_address(self):
        return self.address

grand_child = GrandChild("Misho Kopchev", 19, "Address 15-17")
print(grand_child.name)     # 'Grand Name'
print(grand_child.age)      # '19'
print(grand_child.address)  # 'Address 15-17'