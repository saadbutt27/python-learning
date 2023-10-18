import pygame

class King:
    """A class to manage the king."""

    def __init__(self, ai_game):
        """Initialize the king and set its start position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/king.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a float for the  ship's exact horizontal movement.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update teh ship's position based on movement flag"""
        # Update the ship's x value not the rect. 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.king_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= 1
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        # Update the rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
