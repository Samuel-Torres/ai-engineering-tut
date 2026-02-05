"""Inheritance in Python allows a class to inherit attributes and methods from another class. The class that inherits is called the child class, and the class being inherited from is called the parent class. This promotes code reusability and allows for a hierarchical structure in object-oriented programming."""

# class ElectricCarSpecs:
#     """A class to hold electric car specifications."""

#     def __init__(self, battery_capacity, range_per_charge, charging_time, motor_power):
#         self.battery_capacity = battery_capacity  # in kWh
#         self.range_per_charge = range_per_charge  # in km
#         self.charging_time = charging_time  # in hours
#         self.motor_power = motor_power  # in kW


# class RegularCarSpecs:
#     """A class to hold regular car specifications."""

#     def __init__(self, fuel_tank_capacity, mileage, cyclinder_count, horsepower):
#         self.fuel_tank_capacity = fuel_tank_capacity  # in liters
#         self.mileage = mileage  # in km/l
#         self.cyclinder_count = cyclinder_count
#         self.horsepower = horsepower


class Car:
    """A simple car class."""

    wheel_count = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"The engine of the {self.make} {self.model} is starting."


class ElectricCar(Car):
    """A simple electric car class that inherits from Car."""

    wheel_count = Car.wheel_count  # Inheriting class variable from parent class

    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.battery_capacity = battery_capacity

    def describe(self):
        return f"This is an electric car: {self.make} {self.model} with a battery capacity of {self.battery_capacity} kWh."

    def start_engine(self):
        return (
            f"The electric engine of the {self.make} {self.model} is starting silently."
        )

    def charge_battery(self):
        return f"The battery of the {self.make} {self.model} is charging. Capacity: {self.battery_capacity} kWh."


class HybridCar(Car):
    """A simple hybrid car class that inherits from Car."""

    wheel_count = Car.wheel_count  # Inheriting class variable from parent class

    def __init__(self, make, model, fuel_efficiency):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.fuel_efficiency = fuel_efficiency

    def describe(self):
        return f"This is a hybrid car: {self.make} {self.model} with a fuel efficiency of {self.fuel_efficiency} km/l."

    def start_engine(self):
        return f"The hybrid engine of the {self.make} {self.model} is starting with a combination of fuel and electric power."

    def display_fuel_efficiency(self):
        return f"The fuel efficiency of the {self.make} {self.model} is {self.fuel_efficiency} km/l."


tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.describe())
print(tesla.start_engine())
print(tesla.charge_battery())
print("Tesla Wheel count:", tesla.wheel_count)

print("\n")

toyota = HybridCar("Toyota", "Prius", 25)
print(toyota.describe())
print(toyota.start_engine())
print(toyota.display_fuel_efficiency())
print("Toyota Wheel count:", toyota.wheel_count)
