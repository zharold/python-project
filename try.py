from math import sqrt

class Point:
    def __init__( self, x=2.0 , y=9.0 ):
        self.x =x
        self.y =y

    def __str__(self):
        return "({},{})".format(self.x,self.y)

    def distance_from_origin(self):
        d = sqrt(self.x **2 + self.y **2)
        return d
    def __eq__(self,p):
        return self.x == p.x and self.y == p.y

    def __add__(self,q):
        return "{},{}".format(self.x + self.q,self.y + self.q)

##if "__name__" == "__main__":

p=Point(x=3.4,y=5.6)
print("p.x={}, p.y={}".format(p.x,p.y))
##p = Point(x=3.4,y=5.6)
##print("p.x={}, p.y={}".format(p.x,p.y))
print("p={}".format(p))


q = Point(x=3.4,y=5.6)
print("p.x={},p.y={}".format(p.x,p.y))

print(p.distance_from_origin())
print(p == q)