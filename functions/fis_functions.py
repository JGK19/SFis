from .math_functions import distance

def force(body1, body2, distance_func, norm_func, G=1):
    f = G * (body1.mass * body2.mass) / (distance_func(body1.pos, body2.pos, norm_func)**2)
    return f
