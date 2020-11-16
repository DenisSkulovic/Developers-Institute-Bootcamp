from math import pi
import random


# # Exercise 1:
class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.perimeter = None
        self.area = None

    def compute_perimeter(self):
        self.perimeter = 2 * pi * self.radius

    def compute_area(self):
        self.area = pi * pow(self.radius, 2)

    def geometrical_definition(self):
        print(f"The circle has radius of {self.radius}, perimeter of {self.perimeter} and area of {self.area}.")

c1 = Circle(10)
c1.compute_perimeter()
c1.compute_area()
c1.geometrical_definition()



# # Exercise 2:
class MyList:

    def __init__(self, my_list):
        if type(my_list) == list:
            if len(my_list) > 0:
                self.my_list = my_list
            else:
                print("my_list cannot be of zero length")
                return None
        else:
            print("my_list has to be of type 'list'")
            return None

    def reversed(self):
        return self.my_list[::-1]

    def sorted(self):
        return sorted(self.my_list)

    def random(self):
        return [random.randint(0, 10) for i in range(len(self.my_list))]

mylist = MyList([10,207,3654,24,345,6,754,8,29,10])


