import numpy as np
import pygame


WIDTH, HEIGHT = 800, 600 # Window size 
FPS = 60 # Refresh Rate 
PARTICLE_RADIUS = 20 
PROTON_COLOR = (255, 0, 0) 

class Proton:
    def __init__(self, pos, vel):
        self.pos = np.array(pos, dtype=float) # Array for position
        self.vel = np.array(vel, dtype=float) # Array for velocity 
        self.mass = 1.0 # Constant mass 

    def update(self, dt):
        self += self.vel * dt # Change in displacemeent 

    def draw(self, screen):
        pygame.draw.circle(screen, PROTON_COLOR, self.pos.astype(int), PARTICLE_RADIUS) # Drawing particle on the screen 

    def collide(p1,p2):
        delta = p1.pos - p2.pos
        dist = np.linalg.norm(delta) # Centre to centre distance 

        if dist < 2 * PARTICLE_RADIUS: # Collision if circles overlap/touch
            normal = delta / dist
