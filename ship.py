import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Start each new ship in the middle of left side of the screen 
        self.rect.midleft = self.screen_rect.midleft
        # store a float for ship's exact vertical position
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False
        
    def belitme(self):
        self.screen.blit(self.image, self.rect)    
        
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y
        