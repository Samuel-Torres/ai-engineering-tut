"""
generators are a type of iterable, like lists or tuples. Unlike lists, they do not store their contents in memory; instead, they generate the items on-the-fly and only when requested. This makes them more memory efficient for large datasets.

Decorators are a way to modify or enhance functions or methods without changing their actual code. They are often used for logging, access control, instrumentation, and caching.
"""

# basics of generators:


def serve_chai():
    """A simple generator function that yields Cup 1: different types of chai."""
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"
    yield "Cup 4: Tulsi Chai"


stall = serve_chai()

""" In memory, generators don't use space in memory to store all values at once. Instead, they generate each value on-the-fly when called up in this example when the for loop runs instead. This makes them more memory efficient for large datasets. """

# for cup in stall:
#     print(cup)


def get_chai_list():
    """A simple function that returns a list of different types of chai."""
    return ["cup 1", "cup 2", "cup 3", "cup 4"]


def get_chai_generator():
    """A generator function that yields different types of chai."""
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"
    yield "cup 4"


chai = get_chai_generator()
print(chai)
print(f"GENERATOR: {next(chai)}")
print(f"GENERATOR: {next(chai)}")


print(f"STANDARD: {get_chai_list()}")

# infinite generator example:

# use case: real-time data streams, such as sensor data or user activity logs, where data is continuously generated and needs to be processed on-the-fly. Like a autonomouse car's sensor data.


def infinite_chai():
    counter = 1
    while True:
        yield f"Cup refill: {counter}"
        counter += 1


refill = infinite_chai()

for _ in range(5):
    print(next(refill))


# Sending values to a generator:


def chai_customer():
    print("Welcome, What chai would you like?")
    order = yield  # waits for value to be sent via .send() method.
    while True:
        print(f"Preparing your {order}...")
        order = yield f"Here is your {order}. What would you like next?"
        # pauses and waits for the next order
        # with out this yeild statement, an infinite loop would occur.


stall = chai_customer()
next(stall)  # Start the generator
print(stall.send("Masala Chai"))
print(stall.send("Ginger Chai"))
