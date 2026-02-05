"""
Name Space is a container that holds a set of identifiers (names) and their corresponding objects. In Python, namespaces are implemented as dictionaries that map names to objects. Different types of namespaces exist in Python, including:
- Built-in namespace: Contains built-in functions and exceptions.
- Global namespace: Contains names defined at the module level.
- Local namespace: Contains names defined within a function or method.
"""


class Chai:
    """A simple chai class."""

    origin = "India"  # class variable


print(Chai.origin)  # Accessing class variable without creating an instance.
Chai.is_hot = True  # Adding a new class variable dynamically.
print(Chai.is_hot)

# creating objects from the class:
masala_chai = Chai()
print(
    {
        "origin": masala_chai.origin,
        "is_hot": masala_chai.is_hot,
    }
)

masala_chai.is_hot = False
masala_chai.flavor = "Spicy"


print(masala_chai.flavor, masala_chai.is_hot)
