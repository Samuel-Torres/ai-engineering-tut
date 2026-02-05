"""
Stattic Methods vs Class Methods in Python:
- Static Methods: These methods do not require access to the instance (self) or class (cls) and are defined using the @staticmethod decorator. They behave like regular functions but belong to the class's namespace.
- Class Methods: These methods require access to the class itself and are defined using the @classmethod decorator. They take cls as the first parameter and can access class variables and methods.


"""


class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        # Loads key values from a dictionary to the class constructor above.
        return cls(order_data["tea_type"], order_data["sweetness"], order_data["size"])

    @classmethod
    def from_string(cls, order_string):
        # Loads key values from a string to the class constructor above.
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)


class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(ChaiUtils.is_valid_size("Medium"))  # True - can be used with if clauses etc.


order1 = ChaiOrder.from_dict(
    {"tea_type": "Masala", "sweetness": "Medium", "size": "Large"}
)
print(f"Order 1: {order1.tea_type}, {order1.sweetness}, {order1.size}")

order2 = ChaiOrder.from_string("Ginger-High-Small")
print(f"Order 2: {order2.tea_type}, {order2.sweetness}, {order2.size}")
