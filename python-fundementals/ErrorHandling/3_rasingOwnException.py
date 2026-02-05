"""
How to raise your own exceptions in Python by defining custom exception classes.
"""


class ChaiFlavorError(Exception):
    """Custom exception for invalid chai flavor."""

    pass


class ChaiStrengthError(Exception):
    """Custom exception for invalid chai strength."""

    pass


def brew_chai(flavor: str, strengt: int):
    """Function to brew chai with given flavor and strength."""

    available_flavors = ["Masala", "Ginger", "Tulsi", "Cardamom"]

    if flavor not in available_flavors:
        raise ChaiFlavorError(f"Flavor '{flavor}' is not available.")
    if strengt < 1 or strengt > 5:
        raise ChaiStrengthError("Strength must be between 1 and 5.")
    return f"Brewed a {flavor} chai with strength {strengt}."


# Test cases
orders = [("Masala", 3), ("Lemon", 2), ("Ginger", 6), ("Tulsi", 4)]
for flavor, strength in orders:
    try:
        result = brew_chai(flavor, strength)
    except ChaiFlavorError as cfe:
        print(f"ChaiFlavorError: {cfe}")
    except ChaiStrengthError as cse:
        print(f"ChaiStrengthError: {cse}")
    else:
        print(result)
    finally:
        print("Thank you for choosing our chai stall!\n")
