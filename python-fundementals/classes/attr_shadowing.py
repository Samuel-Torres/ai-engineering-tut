"""
Attribute Shadowing occurs when an instance variable has the same name as a class variable. In such cases, the instance variable "shadows" or overrides the class variable for that particular instance. This means that when you access the attribute on the instance, Python will first look for the instance variable before checking the class variable.
"""


class Chai:
    """A simple chai class."""

    temperature = "Hot"
    strength = "Strong"
    # size = "Medium" # uncomment this line to avoid AttributeError later.


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Warm"
print(cutting.temperature)
print(Chai.temperature)  # Accessing class variable directly from the class.

del cutting.temperature  # Deleting the instance variable.
print("CUTTING AFTER DELETE: ", cutting.temperature)

cutting.size = "Large"
print(cutting.size)
del cutting.size
print(
    "Size after delete: ", cutting.size
)  # This will raise an AttributeError since size is deleted.
