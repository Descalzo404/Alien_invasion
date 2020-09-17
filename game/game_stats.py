class GameStats():
    """Stores the statistic data of the Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize the statistical data"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize the statistical data that can be changed"""
        self.ships_left = self.ai_settings.ship_limit
        