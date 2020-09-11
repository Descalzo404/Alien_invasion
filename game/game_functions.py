import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Answer to when the key is pressed"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        

def check_keyup_events(event, ship):
    """Answer to when the key is released"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
         ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Answer for events in the keyboard or mouse"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Updates the screen"""
    #Redraw the screen in every loop
    screen.fill(ai_settings.bg_color)
    #Redraw every bullet behind the spaceship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    #Displays the most recent screen
    pygame.display.flip()

def update_bullets(bullets):
    """Upadtes the position of the bulllet and delete old bullets"""
    #Updates bullet position
    bullets.update()
    #Delete the projectiles that reached the end of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if the limit isnt surpassed"""
    #Creates a new bullet and add it to the group of bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    