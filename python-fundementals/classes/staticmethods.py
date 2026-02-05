"""
Static methods in Python are methods that belong to a class rather than an instance of the class. They do not require access to instance-specific data (i.e., they don't use 'self'). Static methods are defined using the @staticmethod decorator.
"""


class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        """Static method to clean ingredients."""
        return [item.strip() for item in text.split(",")]


raw_ingredients = " tea leaves , milk , sugar , spices "

cleaned = ChaiUtils.clean_ingredients(raw_ingredients)
print("Cleaned Ingredients:", cleaned)
