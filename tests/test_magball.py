import unittest
import math

from magball_project.ball import Ball
from magball_project.engine import PhysicsEngine

class TestMagballPhysicsEngine(unittest.TestCase):        
    def test_add_ball(self):
        self.engine = PhysicsEngine(dt=1/60, k=900)
        ball = Ball(radius=10, x=0, y=0, xVel=0, yVel=0, charge=1.0, color=(255, 0, 0), weight=1.0)
        self.engine.add_ball(ball)
        self.assertEqual(len(self.engine.bodies), 1)
        body = self.engine.bodies[0]
        self.assertEqual(body.position, (0, 0))
        self.assertEqual(body.velocity, (0, 0))
        
    def test_opposite_charges_attraction(self):
        self.engine = PhysicsEngine(dt=1/60, k=900)
        ball1 = Ball(radius=10, x=-50, y=0, xVel=0, yVel=0, charge=1.0, color=(255, 0, 0), weight=1.0)
        ball2 = Ball(radius=10, x=50, y=0, xVel=0, yVel=0, charge=-1.0, color=(0, 0, 255), weight=1.0)
        self.engine.add_ball(ball1)
        self.engine.add_ball(ball2)
        pos1_before = (ball1.x, ball1.y)
        pos2_before = (ball2.x, ball2.y)
        
        for _ in range(10):
            self.engine.timestep()
        
        states = self.engine.get_states()
        pos1_after = states[0][:2]
        pos2_after = states[1][:2]
        
        self.assertLess(math.dist(pos1_after, pos2_after), math.dist(pos1_before, pos2_before))
        
    def test_like_charges_repulsion(self):
        self.engine = PhysicsEngine(dt=1/60, k=900)
        ball1 = Ball(radius=10, x=-50, y=0, xVel=0, yVel=0, charge=1.0, color=(255, 0, 0), weight=1.0)
        ball2 = Ball(radius=10, x=50, y=0, xVel=0, yVel=0, charge=1.0, color=(0, 0, 255), weight=1.0)
        self.engine.add_ball(ball1)
        self.engine.add_ball(ball2)
        pos1_before = (ball1.x, ball1.y)
        pos2_before = (ball2.x, ball2.y)
        
        for _ in range(10):
            self.engine.timestep()
        
        states = self.engine.get_states()
        pos1_after = states[0][:2]
        pos2_after = states[1][:2]
        
        self.assertGreater(math.dist(pos1_after, pos2_after), math.dist(pos1_before, pos2_before))
        
if __name__ == "__main__":
    unittest.main()
        