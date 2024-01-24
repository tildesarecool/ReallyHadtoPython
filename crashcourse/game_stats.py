class GameStats:
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        # this "left" refers to how many are left...not being on the left side...
        self.ships_left = self.settings.ship_limit