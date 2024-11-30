import pygame
import random
from constants import*
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt    
    
    def is_visible(self, screen):
        screen_width, screen_height = screen.get_size()
        return 0 <= self.position.x <= screen_width and 0 <= self.position.y <= screen_height
