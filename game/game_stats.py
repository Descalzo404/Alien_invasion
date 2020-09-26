class GameStats():
    """Stores the statistic data of the Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize the statistical data"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Initialize the game in an inactive state
        self.game_active = False
        #High score should never be restarted
        self.high_score = 0

    def reset_stats(self):
        """Initialize the statistical data that can be changed"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        