import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):



    def __init__(self, ai_game):


        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/bull.bmp')
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop


        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        # Обновление позиции снаряда в вещественном формате.

        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):

        self.screen.blit(self.image, self.rect)