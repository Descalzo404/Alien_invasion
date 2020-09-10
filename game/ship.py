import pygame

class Ship():
    """A class for the spaceship"""

    def __init__(self, ai_settings, screen):
        """Starts the spaceship and defines its position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the spaceship image
        self.image = pygame.image.load("game\images\ship.bmp")

        #Initialize the rectangules for the spaceship and the screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start the spaceship in the centerx and bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Keeps a float value for the center of the spaceship
        self.center = float(self.rect.centerx)

        #Moviment's flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the position of the spaceship"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        #updates the object rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the spaceship in its actual position"""
        self.screen.blit(self.image,self.rect)