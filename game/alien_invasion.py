import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    #Starts the game and create an object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    #Creates the spaceship
    ship = Ship(screen)

    #Starts the main game loop
    while True:

        #Check for events in keyboard or mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw the screen
        screen.fill(ai_settings.bg_color)
        #Displays the spaceship
        ship.blitme()

        #Displays the most recent screen
        pygame.display.flip()

run_game()