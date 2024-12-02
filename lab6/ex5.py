class Animal:
    def __init__(self, age=0, weight=0):
        self.age = age
        self.weight = weight

class Mammal(Animal):
    def __init__(self, age=0, weight=0, max_speed=0):
        super().__init__(age, weight)
        self.max_speed = max_speed

    def walk(self):
        print(f"Walking with max speed : {self.max_speed} km/h")

class Fish(Animal):
    def __init__(self, age=0, weight=0,  max_depth_swimming=0):
        super().__init__(age, weight)
        self.max_depth_swimming = max_depth_swimming

    def swim(self):
        print(f"Swimming with max depth : {self.max_depth_swimming} m")

class Bird(Animal):
    def __init__(self, age=0, weight=0, wingspan=0):
        super().__init__(age, weight)
        self.wingspan = wingspan

    def fly(self):
        print(f"Flying with wingspan : {self.wingspan} m")

mammal = Mammal(5, 50, 60)
fish = Fish(2, 10, 100)
bird = Bird(3, 2, 1.5)

print("Mammal:")
mammal.walk()

print("\nFish:")
fish.swim()

print("\nBird:")
bird.fly()
