# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from player import Player
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #add player to both groups
    Player.containers = (updatable, drawable)
    # Create the player
    newPlayer = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Create group
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #add shots to group
    Shot.containers = (shots, updatable, drawable)
    # add asteroid to group
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    # create the asteroid field obj
    newAsteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color('black'))

        # Draw the player
        for obj in updatable:
            obj.update(dt)
            #check if shots outside screen despawn them
            if isinstance(obj, Shot) and not obj.is_visible(screen):
                updatable.remove(obj)
            #check for collision between asteroid and player
            for rock in asteroids:
                if newPlayer.collision_check(rock):
                    print("Game over!")
                    pygame.quit()
                    sys.exit()
                for bullet in shots:
                    if bullet.collision_check(rock):
                        bullet.kill()
                        rock.split()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
	main()
