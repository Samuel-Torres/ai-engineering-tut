"""
Decorators in Python are a way to modify or enhance the behavior of functions or methods without changing their actual code. They are often used for logging, access control, instrumentation, and caching, among other things.

Think about it like adding whip cream to a coffee.

"""

from functools import wraps

# basics:


def make_strong(func):
    """A simple decorator that adds 'Strong' to the output of the decorated function."""

    @wraps(func)
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function. Now it's Strong!")

    return wrapper


@make_strong  # Decorating the function with @make_strong, the following function is passed to make_strong as an argument decorator.
def greet():
    """A simple function that greets."""
    print("Hello, enjoy your chai!")


# greet()  # Calling the decorated function.
# print("Name of the function is :", greet.__name__)  # Output: greet


# Logging decorator example:


def log_activity(func):
    """A decorator that logs the activity of the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"Logging: Calling: '{func.__name__}' with arguments {args} and keyword arguments {kwargs}."
        )
        result = func(*args, **kwargs)
        print(f"Logging: Function '{func.__name__}' completed.")
        return result

    return wrapper


@log_activity
def brew_chai(type_of_chai, sugar_level):
    """A function that brews chai of a specific type and sugar level."""
    print(f"Brewing a cup of {type_of_chai} chai with {sugar_level} sugar.")
    return f"{type_of_chai} chai ready!"


# res = brew_chai("Masala", "medium")
# print(res)


# Authorization decorator example:
def require_admin(func):
    """A decorator that checks if the user is an admin."""

    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Authorization Error: User is not authorized to perform this action.")
            return None
        return func()

    return wrapper


@require_admin
def access_admin_panel():
    """A function that simulates accessing an admin panel."""
    print("Accessing the admin panel...")
    return "Admin panel accessed."


print(access_admin_panel("guest"))  # Should print an authorization error.
print(access_admin_panel("admin"))  # Should allow access to the admin panel.
