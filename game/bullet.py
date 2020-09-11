import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that manages the bullets fired from the spaceship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet in the actual position of the spaceship"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a rectangule for the bullet in (0,0) and then defines its correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Keeps the position of the bullet like a float value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet to the top of the screen"""
        #Updates the float position of the bullet
        self.y -= self.speed_factor
        #Updates the position of the rectangule
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)