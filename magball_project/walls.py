from typing import List

class Walls:

    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def checkIfCollision(self, x: float, y: float, radius: float) -> bool:
        if x - radius < self.topLeft[0] or x + radius > self.bottomRight[0]:
            return True
        if y - radius < self.topLeft[1] or y + radius > self.bottomRight[1]:
            return True
        return False
    
