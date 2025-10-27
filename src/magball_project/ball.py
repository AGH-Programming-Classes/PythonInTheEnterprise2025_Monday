class Ball:
    def __init__(self, radius, x, y, xVel, yVel, charge, color, weight):
        self.radius = radius
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.charge = charge
        self.color = color
        self.weight = weight
        
    @property
    def position(self):
        return Pair(self.x, self.y)
    
    @position.setter
    def position(self, pos):
        self.x = pos.a
        self.y = pos.b
    #TODO engine

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a
        self.y = b
    
    def __add__(self, other):
        result = Pair(self.a + other.a, self.b + other.b)
        return result

    def __sub__(self, other):
        result = Pair(self.a - other.a, self.b - other.b)
        return result
    
    def get_length_sqrd(self):
        return self.a ** 2 + self.b ** 2
    
    def normalized(self):
        length = (self.get_length_sqrd()) ** 0.5
        if length == 0:
            return Pair(0, 0)
        result = Pair(self.a / length, self.b / length)
        return result
    
    def __mul__(self, scalar):
        result = Pair(self.a * scalar, self.b * scalar)
        return result