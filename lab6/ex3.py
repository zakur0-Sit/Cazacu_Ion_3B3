class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, milage=0, towing_capacity=0):
        super().__init__(make, model, year)
        self.milage = milage
        self.towing_capacity = towing_capacity

    def calculate_milage(self):
        if self.year < 2000:
            return round(self.milage * 1.5)
        return self.milage

    def calculate_towing_capacity(self):
        if self.year < 2000:
            return self.towing_capacity - 100
        return self.towing_capacity

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, milage=0):
        super().__init__(make, model, year)
        self.milage = milage

    def calculate_milage(self):
        if self.year < 2000:
            return round(self.milage * 1.4)
        return self.milage

class Truck(Vehicle):
    def __init__(self, make, model, year, milage=0, towing_capacity=0):
        super().__init__(make, model, year)
        self.milage = milage
        self.towing_capacity = towing_capacity

    def calculate_milage(self):
        if self.year < 2000:
            return round(self.milage * 1.7)
        return self.milage

    def calculate_towing_capacity(self):
        if self.year < 2000:
            return self.towing_capacity - 150
        return self.towing_capacity

car = Car("Toyota", "Corolla", 2010, 12, 1000)
motorcycle = Motorcycle("Honda", "CBR", 1995, 6)
truck = Truck("Volvo", "FH16", 2018, 21, 2000)

print("Car : ")
print(car)
print("Milage : " + str(car.calculate_milage()) + " l/100km")
print("Towing capacity : " + str(car.calculate_towing_capacity()) + "kg")

print("\nMotorcycle : ")
print(motorcycle)
print("Milage : " + str(motorcycle.calculate_milage()) + " l/100km")

print("\nTruck : ")
print(truck)
print("Milage : " + str(truck.calculate_milage()) + " l/100km")
print("Towing capacity : " + str(truck.calculate_towing_capacity()) + "kg")
