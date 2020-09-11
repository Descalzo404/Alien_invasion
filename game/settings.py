class Settings():
    #A class to keep all settings from the game

    def __init__(self):
        """Start the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Spaceship configuration
        self.ship_speed_factor = 1.5

        #Bullet configuration
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3