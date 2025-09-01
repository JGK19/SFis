import pygame
import sys
from config import WIDTH, HEIGHT, FPS, TITLE, BG_COLOR
from astrobody import AstroBody
from solarSystem import SolarSystem

class Simu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta_t = 1 #self.clock.tick(FPS)/1000000000
        self.running = True

        # sistema = SolarSystem(500000)
        # self.planets = sistema.gen_planets()
        # self.planets = [AstroBody((450, 450), 10, 30, (255, 0, 0), init_v=(-1, -1)), 
        #                 AstroBody((300, 450), 10, 1, (0, 255, 0)), 
        #                 AstroBody((400, 450), 10, 1, (0, 0, 255), init_v=(0, -1.5))]
        # self.planets = [AstroBody((450, 450), 10, 10, (255, 0, 0), init_v=(0, -0.5)), 
        #                 AstroBody((300, 450), 10, 83, (0, 255, 0))]
        # self.planets = [AstroBody((400, 400), 10, 1, (255, 0, 0), init_v=(1, 0)), 
        #                  AstroBody((300, 400), 10, 83, (0, 255, 0))]
        self.planets = [AstroBody((300, 300), 10, 10, (255, 0, 0), init_v=(0, 0)), 
                        AstroBody((500, 500), 10, 10, (0, 255, 0)), 
                        AstroBody((300, 700), 10, 10, (0, 0, 255),)]
        # self.planets = [
        #                 AstroBody((600, 400), 10, 100, (255, 0, 0), init_v=(0, 0)), 
        #                 AstroBody((500, 400), 10, 15, (0, 255, 0), init_v=(0, 1)), 
        #                 AstroBody((700, 400), 10, 15, (0, 0, 255), init_v=(0, -1)),
        #                 #AstroBody((600, 300), 10, 10, (0, 255, 255), init_v=(-1, 0)),
        #                 #AstroBody((600, 500), 10, 10, (255, 0, 255), init_v=(1, 0)),
        #                 ]
        # self.planets = [
        #                 AstroBody((400, 400), 10, 250, (255, 0, 0), init_v=(0, -0.5)), 
        #                 AstroBody((500, 400), 10, 80, (0, 255, 0), init_v=(0, 1)), 
        #                 AstroBody((600, 400), 10, 1, (0, 0, 255), init_v=(0, 1)),
        #                 AstroBody((300, 400), 10, 1, (0, 255, 255), init_v=(0.1, 0)),
        #                 AstroBody((400, 500), 10, 1, (255, 0, 255), init_v=(0.5, 0)),
        #                 ]
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
            p.reset_force()
            for b in self.planets:
                if p is not b:
                    p.apply_gravity(b)
                    p.collision(b, self.delta_t)
            p.update(self.delta_t)
    def draw(self):
        self.screen.fill(BG_COLOR)

        for p in self.planets:
            p.draw(self.screen)

        pygame.display.flip()

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()
