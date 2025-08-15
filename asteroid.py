from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y

    def draw(self,screen):
        color = 255,255,255
        pygame.draw.circle(screen, color,self.position,self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self,asteroidField):
        old_radius = self.radius

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = old_radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20,50)

        angle1 = random_angle
        angle2 = -random_angle

        asteroidField.spawn(new_radius,self.position,self.velocity.rotate(angle1) * 1.2)
        asteroidField.spawn(new_radius,self.position,self.velocity.rotate(angle2) * 1.2)



