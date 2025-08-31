import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de gravidade")

LIGHT_BLUE = (135, 206, 235)
BLUE = (135, 206, 235)
BLACK = (0, 0, 0)
GREEN = (66, 105, 47)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
DARK_GREY = (80, 78, 81)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)
YELLOWISH = (238, 173, 45)
DARK_BLUE = (0, 100, 255)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    TIME = 3600 * 24
    SCALE = 50 / AU

    def __init__(self, radius, color, mass, x, y):

        self.radius = radius
        self.color = color
        self.mass = mass
        self.x = x
        self.y = y

        self.sun = False
        self.distance_to_sun = 0

        self.velocity_x = 0
        self.velocity_y = 0

    def draw(self, win):

        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.velocity_x += total_fx / self.mass * self.TIME
        self.velocity_y += total_fy / self.mass * self.TIME

        self.x += self.velocity_x * self.TIME
        self.y += self.velocity_y * self.TIME

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(20, YELLOW, 1.98892 * 10 ** 30, 0, 0)
    sun.velocity_y = 1 * 1000

    earth = Planet(5, BLUE, 5.9742 * 10 ** 24, -1 * Planet.AU, 0)
    earth.velocity_y = 30 * 1000

    mars = Planet(3, RED, 6.39 * 10 ** 23, -1.524 * Planet.AU, 0)
    mars.velocity_y = 25 * 1000

    mercury = Planet(8, DARK_GREY, 3.30 * 10 ** 23, 0.387 * Planet.AU, 0)
    mercury.velocity_y = -50 * 1000

    venus = Planet(5, WHITE, 4.8685 * 10 ** 24, 0.723 * Planet.AU, 0)
    venus.velocity_y = -35 * 1000

    jupiter = Planet(30, BROWN, 1.898 * 10 ** 27, -5.2 * Planet.AU, 0)
    jupiter.velocity_y = 10 * 1000

    saturn = Planet(20, YELLOWISH, 5.683 * 10 ** 26, 9.5 * Planet.AU, 0)
    saturn.velocity_y = 10 * 1000

    uranus = Planet(10, LIGHT_BLUE, 8.681 * 10 ** 25, -19 * Planet.AU, 0)
    uranus.velocity_y = 10 * 1000

    neptune = Planet(10, DARK_BLUE, 1.024 * 10 ** 26, 30 * Planet.AU, 0)
    neptune.velocity_y = 10 * 1000

    carlos = Planet(10, (255, 0, 255), (1.98892 * 10 ** 30) * 4, 1.2 * Planet.AU , 0)


    planets = [sun, earth, mars, mercury, venus, uranus, saturn, jupiter]

    while run:

        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()