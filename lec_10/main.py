import vehicle

class Car(vehicle.Vehicle):
    def __init__(self, car_weight, car_speed):
        super().__init__(car_weight)
        self.speed = car_speed

    def move(self):
        print("A car is in motion.")

class Plane(vehicle.Vehicle):
    def __init__(self, plane_weight, plane_speed, engine_count):
        super().__init__(plane_weight)
        self.speed = plane_speed
        self.engine_count = engine_count

    def move(self):
        print("A plane is flying.")

class Boat(vehicle.Vehicle):
    def __init__(self, boat_weight, boat_speed, max_load):
        super().__init__(boat_weight)
        self.speed = boat_speed
        self.max_load = max_load

    def move(self):
        print("A boat is sailing.")

class RaceCar(Car):
    def __init__(self, racecar_weight, racecar_speed, horsepower):
        super().__init__(racecar_weight, racecar_speed)
        self.horsepower = horsepower

    def move(self):
        print("A race car is accelerating.")

    def __str__(self):
        return f"A high-performance racecar with weight - {self.weight}, speed - {self.speed}, and horsepower - {self.horsepower} is tearing up the track!"

my_racecar = RaceCar(200, 300, 600)
print(my_racecar)
