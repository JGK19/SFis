import pygame
import numpy as np
from functions.fis_functions import force
from functions.math_functions import norm, distance

class AstroBody:
    
    def __init__(self, init_p, radius, mass, color, init_v=(0,0), init_a=(0,0), distance_func=distance, norm_func=norm, force_func=force):
        self.pos = np.array(init_p, dtype=float)
        self.vel = np.array(init_v, dtype=float)
        self.acc = np.array(init_a, dtype=float)
        self.force = np.array((0, 0), dtype=float)

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
    
    def update(self, delta_t):
        self.pos += (self.vel * delta_t)
        self.vel += (self.acc * delta_t)
        self.acc = (self.force / self.mass)
    
    def collision(self, other_body, delta_t):
        if (distance(self.pos, other_body.pos, self.norm_func) <= self.radius + other_body.radius):
            self.vel = 0

    def apply_gravity(self, other_body):
        direction = other_body.pos - self.pos
        direction = direction / self.norm_func(direction)
        f = self.force_func(self, other_body, self.distance_func, self.norm_func)
        force_vec = direction * f
        self.force += force_vec
    
    def reset_force(self):
        self.force = np.array([0,0], dtype=float)