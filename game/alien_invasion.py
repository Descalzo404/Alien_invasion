import sys

import pygame

def run_game():
    #Starts the game and create an object for the screen
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien invasion")

    #Define the background color
    bg_color = (68,71,90)

    #Starts the main game loop
    while True:

        #Check for events in keyboard or mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw the screen
        screen.fill(bg_color)

        #Displays the most recent screen
        pygame.display.flip()

run_game()