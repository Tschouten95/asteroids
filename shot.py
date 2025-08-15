from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.rotation = 0

    def draw(self,screen):
        color = 255,255,255
        pygame.draw.circle(screen, color,self.position,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

