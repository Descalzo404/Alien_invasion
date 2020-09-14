import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class that represents a single alien in the trrop"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and defines its inicial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Loads the alien image and defines its atribute rect
        self.image = pygame.image.load("game\images\Alien.bmp")
        self.rect = self.image.get_rect()

        #Initialize each new alien in the the top lefft corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Stores the exact position of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien in the actual position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        #Moves the alien for the right
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returns true if the aliens is in the border of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

