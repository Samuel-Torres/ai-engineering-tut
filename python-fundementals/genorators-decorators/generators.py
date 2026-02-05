"""
generators are a type of iterable, like lists or tuples. Unlike lists, they do not store their contents in memory; instead, they generate the items on-the-fly and only when requested. This makes them more memory efficient for large datasets.

keywords: yield, next(), send(), yield from, close()

yield: used in a function to make it a generator. It produces a value and pauses the function's state, allowing it to be resumed later.
next(): retrieves the next value from a generator. It resumes the generator's execution until the next yield statement is encountered.
send(): used to send a value into a generator. It resumes the generator's execution and can
yield from: allows a generator to delegate part of its operations to another generator. It simplifies the code when combining multiple generators.
close(): used to terminate a generator. It raises a GeneratorExit exception inside the generator to perform any necessary cleanup.

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
    # the _ is a convention to indicate that the loop variable is intentionally being ignored.
    print(
        next(refill)
    )  # next() function is used to retrieve the next value from the generator each time it is called.


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

# Yield From example:


def local_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"


def imported_chai():
    yield "Cup A: Tulsi Chai"
    yield "Cup B: Lemon Chai"


def full_menu():
    yield from local_chai()  # delegates to local_chai generator
    yield from imported_chai()  # delegates to imported_chai generator


for chai in full_menu():
    print("FROM FULL: ", chai)


# Close a generator:
def chai_stall():
    try:
        while True:
            order = yield
            print(f"Preparing your {order}...")
    except:
        print("Stall is closing. No more orders can be taken.")


stall = chai_stall()
print(next(stall))  # Start the generator
print(stall.send("Masala Chai"))

stall.close()  # Close the generator: you should always close generators when done using them. Because it releases any resources the generator might be holding onto and ensures that any necessary cleanup code within the generator is executed.
