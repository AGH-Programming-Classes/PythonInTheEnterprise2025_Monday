import random
from magball_project.ball import Ball
from magball_project.graphics import screen_width, screen_height, place_of_board

def create_starting_balls():
    balls = []
    # start positions - zmniejszona odległość dla lepszego efektu
    ball1 = Ball(radius=15, x=place_of_board + 200, y=place_of_board + 200, xVel=0, yVel=0, charge=1, color=(255, 0, 0), weight=1)
    ball2 = Ball(radius=15, x=place_of_board + 500, y=place_of_board + 200, xVel=0, yVel=0, charge=-1, color=(0, 0, 255), weight=1.5)
    balls.append(ball1)
    balls.append(ball2)
    balls.append(Ball(radius=20, x=place_of_board + 350, y=place_of_board + 400, xVel=0, yVel=0, charge=3.2, color=(0, 255, 0), weight=2))
    balls.append(Ball(radius=10, x=place_of_board + 600, y=place_of_board + 300, xVel=0, yVel=0, charge=-5, color=(255, 255, 0), weight=0.5))
    return balls

def create_balls_random():
    output = []
    number = random.randint(2, 10)
    for i in range(number):
        radius = random.randint(5, 30)
        x = random.randint(place_of_board + radius, screen_width - place_of_board - radius)
        y = random.randint(place_of_board + radius, screen_height - place_of_board - radius)
        xVel = random.uniform(-100, 100)
        yVel = random.uniform(-100, 100)
        charge = random.uniform(-10, 10)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        weight = random.uniform(0.5, 5.0)
        output += [Ball(radius=radius, x=x, y=y, xVel=xVel, yVel=yVel, charge=charge, color=color, weight=weight)]
    return output
