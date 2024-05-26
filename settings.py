class Settings():
    def __init__(self):
        """A class to store all the settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = ("purple")
        self.ship_speed = 1.5
        # Bullet Settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # How quickly the game speeds up
        self.speedup_scale = 1.1 
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        