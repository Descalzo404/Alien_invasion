import sys
import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship


def run_game():
    #Starts the game and create an object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")

    #Creates the spaceship
    ship = Ship(ai_settings, screen)
    #Creates a group that stores the bullets
    bullets = Group()
    #Creates a group that stores the aliens
    aliens = Group()

    #Creates the alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Creates the instance to store the game's data
    stats = GameStats(ai_settings)

    #Starts the main game loop
    while True:

        #Check for events in keyboard or mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        #Updates the position of the ship
        ship.update()
        #Update the position of the bullets and clean the bullets that reach the end of the screen
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        #Updates the position of the alien
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        #Display the new screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()