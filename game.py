import pygame
from ship import Ship
from button import Button
from settings import Settings
class Game: 
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height ))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Shoot the target")
        self.ship = Ship(self)
        self.running = True
        self.play_button = Button(self, "Play")
        
    
    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update() 
            self._updateScreen()
            self.clock.tick(60)
            
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                           
    def _updateScreen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.belitme()  
        pygame.display.flip()
        
if __name__ == '__main__':
    gg = Game()
    gg.run_game()
        