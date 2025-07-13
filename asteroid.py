import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Call parent constructor
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_ang = random.uniform(20,50)

            v1 = pygame.math.Vector2.rotate(self.velocity, random_ang)
            v2 = pygame.math.Vector2.rotate(self.velocity, -random_ang)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            A1 = Asteroid(self.position.x, self.position.y, new_radius)
            A2 = Asteroid(self.position.x, self.position.y, new_radius)

            A1.velocity = v1 * 1.2
            A2.velocity = v2 * 1.2



            