# pure vs impure functions:


def pure_chai(cups):
    """Pure function: always returns the same output for the same input and has no side effects."""
    return cups * 2


# not recommended to use global variables
total_chai = 0


def impure_chai(cups):
    """Impure function: modifies a global variable, causing side effects."""
    global total_chai
    total_chai += cups
    print("The value is:", cups)
