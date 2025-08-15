import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    print("asteroid max radius:", ASTEROID_MAX_RADIUS)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidField = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)

    player = Player(
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2
    )

    asteroidField = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        destroyed_asteroids = []
        destroyed_shots = []
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.colliding(asteroid):
                    destroyed_asteroids.append(asteroid)
                    destroyed_shots.append(shot)

        for destroyed_asteroid in destroyed_asteroids:
            destroyed_asteroid.kill()

        for destroyed_shot in destroyed_shots:
            destroyed_shot.kill()

        screen.fill(0)

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
