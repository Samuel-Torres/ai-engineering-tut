"""
3 Ways to Access Base Class Members in Python Inheritance:
Code duplication
explicit call to base class
super() function
"""


class Chai:
    def __init__(self, type, strength):
        self.type = type
        self.length = str(length) + " inches"


class MasalaChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level  # code is duplicated here.


class GingerChai(Chai):
    # You can create the attributes without duplicating code, like this:
    def __init__(self, type_, strength, ginger_amount):
        # explicit call to base class:
        Chai.__init__(self, type_, strength)  # explicit call to base class
        self.ginger_amount = ginger_amount


class LemonChai(Chai):
    # Using super() function to access base class members:
    def __init__(self, type_, strength, lemon_slices):
        # This way, you avoid code duplication:
        super().__init__(type_, strength)  # Using super() function
        self.lemon_slices = lemon_slices
