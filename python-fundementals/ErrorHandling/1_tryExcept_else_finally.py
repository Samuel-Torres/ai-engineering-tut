"""
Try, Except, Else, Finally Example:
"""

chai_menu = {
    "Masala": 3.5,
    "Ginger": 3.0,
    "Tulsi": 4.0,
    "Cardamom": 4.5,
}


def order_chai(chai_type, quantity):
    try:
        price_per_cup = chai_menu[chai_type]
    except KeyError:
        print(f"Sorry, we don't have {chai_type} chai on the menu.")
    else:
        total_cost = price_per_cup * quantity
        print(
            f"Your order for {quantity} cup(s) of {chai_type} chai will cost ${total_cost:.2f}."
        )
    finally:
        print("Thank you for visiting our chai stall!")


# Test cases
order_chai("Masala", 2)  # Valid order
order_chai("Lemon", 1)  # Invalid order
