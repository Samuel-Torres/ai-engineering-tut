# Lamdbas are anonymous functions in Python, often used for short, throwaway functions.

chai_types = ["Masala", "Tulsi", "Ginger", "Cardamom", "Tulsi"]

strong_chai = list(filter(lambda chai: chai == "Tulsi", chai_types))
print("Strong Chai Types:", strong_chai)


nums = [1, 2, 3, 4, 5]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even Numbers:", even_nums)
