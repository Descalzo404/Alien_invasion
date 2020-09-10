import sys
import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    #Starts the game and create an object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    #Creates the spaceship
    ship = Ship(ai_settings, screen)

    #Starts the main game loop
    while True:

        #Check for events in keyboard or mouse
        gf.check_events(ship)
        #Updates the position of the ship
        ship.update()
        #Display the new screen
        gf.update_screen(ai_settings, screen, ship)

run_game()