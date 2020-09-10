import pygame

class Ship():
    """A class for the spaceship"""

    def __init__(self, screen):
        """Starts the spaceship and defines its position"""
        self.screen = screen

        #Load the spaceship image
        self.image = pygame.image.load("game\images\ship.bmp")

        #Initialize the rectangules for the spaceship and the screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start the spaceship in the centerx and bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Moviment's flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the position of the spaceship"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the spaceship in its actual position"""
        self.screen.blit(self.image,self.rect)