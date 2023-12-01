import math  

class Shape: 
    pass 

class TwoDimensionalShape(Shape): 
    def area(self): 
        pass 

class ThreeDimensionalShape(Shape): 
    def area(self): 
        pass 

    def volume(self): 
        pass 

class Square(TwoDimensionalShape): 
    def __init__(self, side_length): 
        self.__side_length = side_length 

    def area(self): 
        return self.__side_length ** 2 

class Triangle(TwoDimensionalShape): 
    def __init__(self, side_a, side_b, side_c): 
        self.__side_a = side_a 
        self.__side_b = side_b 
        self.__side_c = side_c 

    def area(self): 
        p = (self.__side_a + self.__side_b + self.__side_c) / 2 
        return math.sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c)) 

class Cube(ThreeDimensionalShape): 
    def __init__(self, side_length): 
        self.__side_length = side_length 

    def area(self): 
        return 6 * pow(self.__side_length, 2) 

    def volume(self): 
        return self.__side_length ** 3 

class Cone(ThreeDimensionalShape): 
    def __init__(self, radius, height): 
        self.__radius = radius 
        self.__height = height 

    def area(self): 
        return math.pi * self.__radius * (self.__radius + math.sqrt(self.__height ** 2 + self.__radius ** 2))

    def volume(self): 
        return (1/3) * math.pi * (self.__radius ** 2) * self.__height 


my_square = Square(7) 
my_triangle = Triangle(6, 8, 10) 
my_cube = Cube(10) 
my_cone = Cone(4, 10) 

print("Area of square: ", my_square.area()) 
print("Area of triangle: ", my_triangle.area()) 

print("Area of Cube: ", my_cube.area()) 
print("Volume of Cube: ", my_cube.volume()) 

print("Area of Cone: ", my_cone.area()) 
print("Volume of Cone: ", my_cone.volume())
