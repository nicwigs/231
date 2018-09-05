import math
class Vector(object):
    def __init__(self,x=0,y=0):
        self.x = 0
        self.y = 0
        if isinstance(x,float) and isinstance(y,float):
            self.x = x
            self.y = y
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return "Vector: <{},{}>".format(self.x,self.y)
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self,mult):       
        if isinstance(mult,float):           
            return Vector(mult*self.x, mult*self.y)
        elif isinstance(mult,Vector):
            return self.x * mult.x + self.y * mult.y
    def __rmul__(self,mult):
        return self * mult
        