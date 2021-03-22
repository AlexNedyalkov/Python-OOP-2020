"""
    1. Store
Create a class called Store. Upon initialization it should receive a name (str), type (str), capacity (int).
 The store should also have an attribute called items (dictionary that stores name of an item and its quantity).
 The class should have 4 methods:
    • from_size (name:str, type:str, size:int) – a new instance should be created with capacity which is 50% of the size
    • add_item(item_name:str) – adds 1 to the quantity of the given item.
    On success, the method should return "{item_name} added to the store".
    If the addition is not possible, the following message should be returned "Not enough capacity in the store"

    • remove_item(item_name:str, amount:int) – removes the given amount from the item.
     On success, it should return "{count} {item_name} removed from the store".
    Otherwise, the method should return "Cannot remove {count} {item_name}"
    • __repr__() - returns a string representation in the format "{store_name} of type {store_type} with capacity {store_capacity}"
"""
class Store:

    items: dict = {}

    def __init__(self, name: str, type: str, capacity: int):
        self.name: str = name
        self.type: str = type
        self.capacity: int = capacity

    @classmethod
    def from_size(cls, name: str, type: str, size: int):
        return Store(name, type, int(size/2))

    def add_item(self, item_name: str):
        if sum(self.items.values()) == self.capacity:
            return "Not enough capacity in the store"
        if item_name in self.items.keys():
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
            return f"{item_name} added to the store"

    def remove_item(self, item_name:str, amount:int):
        if item_name in self.items.keys() and self.items[item_name] - amount >= 0:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))

"""
Output
First store of type Fruit and Veg with capacity 20
Second store of type Clothes with capacity 250
potato added to the store
jeans added to the store
Cannot remove 1 tomatoes
1 jeans removed from the store

"""