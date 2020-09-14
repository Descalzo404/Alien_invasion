import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Updates the screen"""
    #Redraw the screen in every loop
    screen.fill(ai_settings.bg_color)
    #Redraw every bullet behind the spaceship and the aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Displays the most recent screen
    pygame.display.flip()

def update_bullets(aliens, bullets):
    """Upadtes the position of the bulllet and delete old bullets"""
    #Updates bullet position
    bullets.update()
    #Delete the projectiles that reached the end of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #Verifies if a bullet hit an alien
    #If so, get read of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if the limit isnt surpassed"""
    #Creates a new bullet and add it to the group of bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determines the numebr of rows with aliens fit the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_fleet(ai_settings, screen, ship, aliens):
    """Creates a complete alien fleet"""
    #Creates an alien and calculate the number of aliens in one line
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    

    #Creates the alien fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Creates an alien and puts it in the line
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
    
def get_number_aliens_x(ai_settings, alien_width):
    """Determines the  number of aliens that fit in the row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Creates a alien and positions it in the line
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

def update_aliens(ai_settings, aliens):
    """Verifies if the fleet is in a border and the updates the position of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    """Respond to when a alien reaches the border of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Makes all the fleet go down and changes its direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
