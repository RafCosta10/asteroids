import pygame
import sys

from constants import SCREEN_WIDTH, SHOT_RADIUS
from constants import SCREEN_HEIGHT

from logger import log_state
from logger import log_event

import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    player_1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    
    asteroidfield.AsteroidField.containers = (updatable)
    asteroidfield_1 = asteroidfield.AsteroidField()

    shot.Shot.containers = (shots, drawable, updatable)

    while (True):
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        
        updatable.update(dt)

        player_1.cooldown -= dt

        for item in asteroids:
            if player_1.collides_with(item):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if bullet.collides_with(item):
                    log_event("asteroid_shot")
                    bullet.kill()
                    item.split()
        
        screen.fill("black")
    
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
