"""
Property Decorators are a way to manage the attributes of a class by defining methods that act as getters, setters, and deleters for those attributes. They provide a way to encapsulate the access to an attribute, allowing for validation, computation, or other logic to be executed when getting or setting the attribute's value.
"""


class TeaLeaf:

    def __init__(self, age):
        self._age = age  # Private attribute

    @property
    def age(self):
        """Getter for age property."""
        return self._age + 2  # Adding 2 years to the actual age for processing

    @age.setter
    def age(self, value):
        """Setter for age property with validation."""
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value


leaf = TeaLeaf(3)
print("Tea Leaf Age (with processing):", leaf.age)  # Accessing age via getter
leaf.age = 5  # Setting age via setter
print("Updated Tea Leaf Age (with processing):", leaf.age)
# leaf.age = -5  # Setting age via setter
# print("Updated Tea Leaf Age (with processing):", leaf.age)

leaf._age = 10  # Directly accessing the private attribute
print("Directly Accessed Tea Leaf Age (without processing):", leaf._age)
