from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        color = 255,255,255
        points = self.triangle()
        pygame.draw.polygon(screen,color,points,2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            num = 0 - dt
            self.rotate(num)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            num = 0 - dt
            self.move(num)
        if keys[pygame.K_SPACE]:
            if self.cooldown <= 0:
                self.shoot(dt)
        self.cooldown -= dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(
            self.position,
            self.position,
            SHOT_RADIUS
        )

        shot.velocity += pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
