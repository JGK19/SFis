from astrobody import AstroBody
from functions.fis_functions import force
from functions.math_functions import distance
from config import WIDTH, HEIGHT

class SolarSystem:
    G = 6.674184 * (10**(-11))

    def __init__(self, K):
        self.K = K
    def gen_planets(self):
        K = self.K
        pos_y = HEIGHT/2
        pos_sol = WIDTH/2
        planets = {
            "Sol": AstroBody((pos_sol, pos_y), 20, 1.98892 * (10**30), (255, 255, 0), force_func=self.force_func(self.G)),
            # "Mercúrio": AstroBody((pos_sol + 57910000/K, pos_y), 20, (3.285/K) * (10**23), (100, 100, 100), force_func=self.force_func(self.G)),
            "Vênus": AstroBody((pos_sol + 108200000/K, pos_y), 20, (3.285/K) * (10**23), (200, 150, 50), init_v=(0, 800000000), force_func=self.force_func(self.G)),
            # "Terra": AstroBody((pos_sol + 149600000/K, pos_y), 20, (5.972/K) * (10**24), (0, 150, 100), init_v=(0, 607000000), force_func=self.force_func(self.G)),
            # "Marte": AstroBody((pos_sol + 227940000/K, pos_y), 5, (6.39/K) * (10**23), (255, 0, 0), force_func=self.force_func(self.G)),
            # "Júpiter": AstroBody((pos_sol + 778330000/K, pos_y), 5, (1.898/K) * (10**27), (100, 100, 60), force_func=self.force_func(self.G)),
            # "Saturno": AstroBody((pos_sol + 1429400000/K, pos_y), 5, (5.683/K) * (10**26), (150, 200, 100), force_func=self.force_func(self.G)),
            # "Urano": AstroBody((pos_sol + 2870990000/K, pos_y), 5, (8.681/K) * (10**25), (0, 0, 100), force_func=self.force_func(self.G)),
            # "Netuno": AstroBody((pos_sol + 4504000000/K, pos_y), 5, (1.024/K) * (10**26), (0, 0, 255), force_func=self.force_func(self.G)),
        }
        return planets.values()
    
    @staticmethod
    def force_func(G):
        def force(body1, body2, distance_func, norm_func):
            f = G * (body1.mass * body2.mass) / (distance_func(body1.pos, body2.pos, norm_func)**2)
            return f
        return force