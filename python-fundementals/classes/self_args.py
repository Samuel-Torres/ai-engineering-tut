"""
self arguments are used in class methods to refer to the instance of the class itself. They allow access to the attributes and methods of the class in Python.
"""


class Chai:
    """A simple chai class."""

    def __init__(self, flavor, temperature):
        self.flavor = flavor
        self.temperature = temperature

    def describe(self):
        """Method to describe the chai."""
        return f"This is a {self.temperature} cup of {self.flavor} chai."


masala_chai = Chai("Masala", "Hot")
print(masala_chai.describe())
