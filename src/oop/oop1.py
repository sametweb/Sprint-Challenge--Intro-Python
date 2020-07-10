# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass


class GroundVehicle(Vehicle):  # GroundVehicle is a Vehicle
    pass


class Car(GroundVehicle):  # Car is a GroundVehicle
    pass


class Motorcycle(GroundVehicle):  # Motorcycle is a GroundVehicle
    pass


class FlightVehicle(Vehicle):  # FlightVehicle is a Vehicle
    pass


class Airplane(FlightVehicle):  # Airplane is a FlightVehicle
    pass


class Starship(FlightVehicle):  # Starship is a FlightVehicle
    pass
