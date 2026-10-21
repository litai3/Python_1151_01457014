class Vehicle:
    def __init__(self, brand, year, data):
        self.brand = brand
        self.year = year
        self.data = data


class Car(Vehicle):
    def print_obj(self):
        print(f"Car: {self.brand}, Year: {self.year}, Seat: {self.data}\n")


class Motorcycle(Vehicle):
    def print_obj(self):
        print(f"Motorcycle: {self.brand}, Year: {self.year}, cc: {self.data}\n")


class Bicycle(Vehicle):
    def print_obj(self):
        print(f"Bicycle: {self.brand}, Year: {self.year}, Model: {self.data}\n")


vehicle_list = []
while True:
    inputs = input().strip().split()
    type = ""
    try:
        type, brand, year, data = inputs
    except ValueError:
        op = inputs[0] if len(inputs) > 0 else ""
        if op == "stop":
            break
        elif op == "print":
            for obj in vehicle_list:
                obj.print_obj()

    if type == "Car":
        obj = Car(brand, year, data)
        vehicle_list.append(obj)
    elif type == "Motorcycle":
        obj = Motorcycle(brand, year, data)
        vehicle_list.append(obj)
    elif type == "Bicycle":
        obj = Bicycle(brand, year, data)
        vehicle_list.append(obj)
