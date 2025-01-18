from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, 'white',self.position , self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(angle)
            vector_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(x = self.position.x, y =self.position.y, radius = new_radius)
            asteroid_1.velocity = vector_1 * 1.2

            asteroid_2 = Asteroid(x = self.position.x, y =self.position.y, radius = new_radius)
            asteroid_2.velocity = vector_2 * 1.2