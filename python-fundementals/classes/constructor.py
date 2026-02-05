"""
Class Contructor is a special method in Python used to initialize newly created objects of a class. It is defined using the __init__() method. The constructor is called automatically when an object of the class is instantiated.
"""


class Chai:
    """A simple chai class."""

    def __init__(self, type_, flavor, temperature):
        """Constructor to initialize flavor and temperature of the chai."""
        self.type_ = type_
        self.flavor = flavor
        self.temperature = temperature

    def describe(self):
        """Method to describe the chai."""
        return f"This is a {self.temperature} cup of {self.flavor} {self.type_} chai."


masala_chai = Chai("Masala", "Spicy", "Hot")
print(masala_chai.describe())
