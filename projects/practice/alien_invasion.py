import sys

import pygame

from settings import Settings
from kings import King

class AlienInvasion:
    """Overall class to manage alien assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.king = King(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # self._check_events()
            # self.king.update()
            # self._update_screen()
            # self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)


    def _check_events(self):
        """Responds to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.king.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.king.moving_left = True
        elif event.key == pygame.K_UP:
            self.king.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.king.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.king.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.king.moving_left = False
        elif event.key == pygame.K_UP:
            self.king.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.king.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass thought the loop.
        self.screen.fill(self.settings.bg_color)
        self.king.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
            


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()