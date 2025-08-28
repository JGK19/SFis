import numpy as np

def distance(pos1, pos2, norm_func):
    return norm_func(pos1 - pos2)

def norm(vec):
    return np.sqrt(np.dot(vec, vec))