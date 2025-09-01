import pygame
import numpy as np
from functions.fis_functions import force
from functions.math_functions import norm, distance
import math

def draw_direction_vector(screen, start_pos, vector, length=100, color=(255,0,0), width=3, arrow_size=10):
    dx, dy = vector
    # Normaliza o vetor
    mag = math.hypot(dx, dy)
    if mag == 0:
        return  # vetor nulo, nada a desenhar
    dx_norm = dx / mag
    dy_norm = dy / mag
    
    # Calcula posição final baseada no tamanho fixo
    end_pos = (start_pos[0] + dx_norm * length,
               start_pos[1] + dy_norm * length)  # y cresce para baixo no pygame
    
    # Desenha linha principal
    pygame.draw.line(screen, color, start_pos, end_pos, width)
    
    # Ângulo do vetor
    angle = math.atan2(start_pos[1] - end_pos[1], end_pos[0] - start_pos[0])
    
    # Pontas da seta
    left = (end_pos[0] - arrow_size * math.cos(angle - math.pi/6),
            end_pos[1] + arrow_size * math.sin(angle - math.pi/6))
    right = (end_pos[0] - arrow_size * math.cos(angle + math.pi/6),
             end_pos[1] + arrow_size * math.sin(angle + math.pi/6))
    
    pygame.draw.polygon(screen, color, [end_pos, left, right])

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
        # draw_direction_vector(screen, (x, y), self.force)
        draw_direction_vector(screen, (x, y), self.vel, color=(0,255,0))
    
    def update(self, delta_t):
        self.pos += (self.vel * delta_t)
        self.vel += (self.acc * delta_t)
        self.acc = (self.force / self.mass)
    
    def collision(self, other_body, delta_t):
        if (distance(self.pos, other_body.pos, self.norm_func) <= self.radius + other_body.radius):
            self.vel = np.array([0,0], dtype=float)

    def apply_gravity(self, other_body):
        direction = other_body.pos - self.pos
        direction = direction / self.norm_func(direction)
        f = self.force_func(self, other_body, self.distance_func, self.norm_func)
        force_vec = direction * f
        self.force += force_vec
    
    def reset_force(self):
        self.force = np.array([0,0], dtype=float)