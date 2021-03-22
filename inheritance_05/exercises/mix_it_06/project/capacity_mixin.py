class CapacityMixin:

    @staticmethod
    def get_capacity(capacity, amount):
        if capacity < amount:
            raise Exception("Capacity reached!")
        return capacity - amount