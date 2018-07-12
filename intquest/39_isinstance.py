class Vehicle:
    pass

class Truck(Vehicle):
    pass


isinstance(Vehicle(), Vehicle)  # returns True
type(Vehicle()) == Vehicle      # returns True
print(issubclass(Truck, Vehicle) )   # returns True
type(Truck()) == Vehicle        # returns False, and this probably won't be what you want.