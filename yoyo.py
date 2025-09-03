import numpy as np
import pygame


WIDTH, HEIGHT = 800, 600
FPS = 60
PARTICLE_RADIUS = 20
PROTON_COLOR = (255, 0, 0)

class Proton:
    def __init__(self, pos, vel):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.mass = 1.0 

    def update(self, dt):
        self += self.val * dt