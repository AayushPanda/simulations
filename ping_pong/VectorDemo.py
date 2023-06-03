import math

# Simple Vector class
"""
    A Vector is can be described as a point in space
    It's x & y coordinates are just a point on a plane
    A Vector does not have to be limited to 2 dimensions,
    they can also have z, w, v... axis!
"""
class Vector(object):
    def __init__(self, x: float, y: float):
        self.x: float = x;
        self.y: float = y
    
    # boilerplate str and printing overloading
    def __str__(self) -> str:
        return str("({:.4f}".format(self.x) + ", {:.4f})".format(self.y))

    def __repr__(self) -> str:
        return str("({:.4f}".format(self.x) + ", {:.4f})".format(self.y))
    
    # boilerplate operator overloading
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    # The magnitude of a vector is simply it's length!
    def Magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

def Example():
    a = Vector(10, 10)
    b = Vector(20, 20)
    print(f"a: {a}")
    print(f"A has an x coordinate of {a.x} and a y coordinate of {a.x}")
    print(f"b: {b}")
    print(f"B has an x coordinate of {b.x} and a y coordinate of {b.y}")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print("magnitude of a: {:.4f}".format(a.Magnitude()))
    print("magnitude of b: {:.4f}".format(b.Magnitude()))
    print("magnitude of a + b: {:.4f}".format((a + b).Magnitude()))
    print("magnitude of a - b: {:.4f}".format((a - b).Magnitude()))


Example()