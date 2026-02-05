"""
Handling Multiple Exceptions in Python
"""


def process_order(item: str, quantity: int):
    """Function to process an order."""

    menu = ["Masala", "Ginger", "Tulsi", "Cardamom"]

    if item not in menu:
        raise ValueError("Item not available.")
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if quantity > 10:
        raise OverflowError("Quantity exceeds available stock.")
    return f"Order processed: {quantity} x {item}"


# Test cases
orders = [("Masala", 2), ("Lemon", 1), ("Ginger", -3), ("Tulsi", 15)]
for item, qty in orders:
    try:
        result = process_order(item, qty)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except OverflowError as oe:
        print(f"OverflowError: {oe}")
    else:
        print(result)
    finally:
        print("Please come again soon!\n")
