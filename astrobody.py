import pygame
import numpy as np
from functions.fis_functions import force
from functions.math_functions import norm, distance

class AstroBody:
    G = 1
    
    def __init__(self, init_p, radius, mass, color, init_v=(0,0), init_a=(0,0), distance_func=distance, norm_func=norm, force_func=force):
        self.pos = np.array(init_p, dtype=float)
        self.vel = np.array(init_v, dtype=float)
        self.acc = np.array(init_a, dtype=float)
        self.force = np.array([0, 0], dtype=float)
        self.radius = radius
        self.color = color

        self.mass = mass

        self.distance_func = distance_func
        self.norm_func = norm_func
        self.force_func = force_func

    def draw(self, screen):
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
    
    def update(self):
        self.pos += self.vel
        self.vel += self.acc

    def apply_gravity(self, other_body):
        direction = other_body.pos - self.pos
        direction = direction / self.norm_func(direction)
        f = self.force_func(self, other_body, self.distance_func, self.norm_func)
        force_vec = direction * f
        self.acc = force_vec / self.mass