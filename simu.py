import pygame
import sys
from config import WIDTH, HEIGHT, FPS, TITLE, BG_COLOR
from astrobody import AstroBody

class Simu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.planets = [AstroBody((400, 400), 10, 1, (255, 0, 0), init_v=(-1,-1)), AstroBody((300, 400), 10, 1, (0, 255, 0)),
                        AstroBody((350, 450), 10, 1, (0, 0, 255), init_v=(0, -1))]
    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def update(self):
        for p in self.planets:
            p.update()
            for b in self.planets:
                if p is not b:
                    p.apply_gravity(b)
    def draw(self):
        self.screen.fill(BG_COLOR)

        for p in self.planets:
            p.draw(self.screen)

        pygame.display.flip()

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()
