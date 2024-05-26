import pygame
import sys
from ship import Ship
from button import Button
from settings import Settings
from bullet import Bullet

class Game: 
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height ))
        self.display_rectangle = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Shoot the target")
        self.ship = Ship(self)
        self.running = False
        self.play_button = Button(self, "Play")
        self.rectShape = pygame.Rect(self.display_rectangle.right -120  ,2,5,100)
        self.direction = 1
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        
        while True:
            self._check_events()
            if self.running:
                self.ship.update() 
                self._update_bullets()
                pygame.display.flip()
            self._updateScreen()
            pygame.draw.rect(self.screen,'black',self.rectShape)
            self._update_rect()
            self.clock.tick(60)
            
    def _update_bullets(self):
        self.bullets.update()  
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.display_rectangle.right:
                self.bullets.remove(bullet)
            elif self.rectShape.colliderect(bullet.rect):
                self.bullets.remove(bullet)
                self.rectShape = pygame.Rect(self.display_rectangle.right -120  ,2,5,100)
                # self.running = False
                self.settings.increase_speed()
           
    def _update_rect(self):
        self.rectShape.y += 2 * self.direction
        if self.rectShape.bottom >= self.display_rectangle.bottom:
            self.direction = -1
        if self.rectShape.top <= 0: 
            self.direction = 1    
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings()
            self.running = True
                        
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()   
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
                           
    def _updateScreen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.belitme()  
        if not self.running:
            self.play_button.draw_button()
        pygame.display.flip()
        
if __name__ == '__main__':
    gg = Game()
    gg.run_game()
        