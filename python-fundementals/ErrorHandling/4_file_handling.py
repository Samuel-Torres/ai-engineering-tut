"""
File Handling Example
"""

# open("orders.txt", "w")
# try:
#     file = open("orders.txt", "w")
# finally:
#     file.close()


with open("orders.txt", "w") as file:
    file.write("Order 1: Masala Chai\n")
    file.write("Order 2: Ginger Chai\n")
    file.write("Order 3: Tulsi Chai\n")
