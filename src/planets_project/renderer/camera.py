from src.planets_project.models.planet import Planet

ZOOM_STEP = 1.1  # 10% zoom each time

initial_scale = 250 / Planet.AU
Planet.SCALE = initial_scale

current_scale = Planet.SCALE

def zoom_in():
    global current_scale
    current_scale *= ZOOM_STEP
    Planet.SCALE = current_scale

def zoom_out():
    global current_scale
    current_scale /= ZOOM_STEP
    Planet.SCALE = current_scale
