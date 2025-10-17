import pygame
import pymunk

from magball_project.ball import Ball


class PhysicsEngine:
    def __init__(self, dt: float = 1/60, k: float = 900):
        self.space = pymunk.Space()  
        self.space.gravity = (0, 0)  # No gravity for the top-down look
        self.dt = dt  # Timestep
        self.k = k  # Coulomb's constant equivalent
        self.bodies: list[pymunk.Body] = []  # List of bodies in the simulation

    def add_ball(self, ball: Ball):
        weight = ball.weight if ball.weight > 0 else 1.0  # Prevent zero weight
        moment = pymunk.moment_for_circle(weight, 0, ball.radius)
        body = pymunk.Body(weight, moment)
        body.position = ball.x, ball.y
        body.velocity = ball.xVel, ball.yVel
        shape = pymunk.Circle(body, ball.radius)
        shape.color = pygame.Color(ball.color)
        shape.elasticity = 0.9  # 0.9 instead of 1.0 as recommended
        shape.friction = 0.0  # No friction for top-down
        shape.charge = ball.charge  # Custom attribute for charge
        self.space.add(body, shape)
        self.bodies.append(body)
        
    def timestep(self):
        n = len(self.bodies)
        
        for i in range(n):
            ball_i = self.bodies[i]
            for j in range(i + 1, n):
                ball_j = self.bodies[j]
                ij_vector = pymunk.Vec2d(ball_j.position) - pymunk.Vec2d(ball_i.position)
                dist_sq = ij_vector.get_length_sqrd()
                if dist_sq == 0:
                    continue  # Avoid division by zero
                
                force_magnitude = self.k * (ball_i.shapes[0].charge * ball_j.shapes[0].charge) / dist_sq
                direction = ij_vector.normalized()
                force = direction * force_magnitude
                ball_i.apply_force_at_world_point(force, ball_i.position)
                ball_j.apply_force_at_world_point(-force, ball_j.position)
        self.space.step(self.dt)

