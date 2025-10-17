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
                ij_vector = ball_j.position - ball_i.position
                dist_sq = ij_vector.get_length_sqrd()
                if dist_sq == 0:
                    continue  # Avoid division by zero
                
                shape_i = next(iter(ball_i.shapes))
                shape_j = next(iter(ball_j.shapes))
                charge_i = getattr(shape_i, 'charge', 0.0)
                charge_j = getattr(shape_j, 'charge', 0.0)
                
                force_magnitude = self.k * (charge_i * charge_j) / dist_sq
                direction = ij_vector.normalized()
                force = direction * force_magnitude
                ball_i.apply_force_at_world_point(-force, ball_i.position)
                ball_j.apply_force_at_world_point(force, ball_j.position)
        self.space.step(self.dt)

# Get the current states of all balls for testing
    def get_states(self):
        ball_states = []
        for body in self.bodies:
            shape = next(iter(body.shapes))
            ball_states.append((
                float(body.position.x),
                float(body.position.y),
                float(body.velocity.x),
                float(body.velocity.y),
                getattr(shape, 'charge', 0.0),
                getattr(shape, 'radius', 0.0)
            ))
        return ball_states
