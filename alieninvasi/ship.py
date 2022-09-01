import pygame
from settings import Settings

class Ship():

    def __init__(self, ai_game):

        self.screen = ai_game
        self.settings = Settings()
        self.screen_rect = ai_game.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        #"""Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # Обновление атрибута rect на основании self.x
        self.rect.x = self.x


    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)



    def blitme(self):
        #"""Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)





