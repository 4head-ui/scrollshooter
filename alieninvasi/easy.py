import pygame.font


class Easy():



    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()



        self.width, self.height = 100, 30
        self.button_color = (0, 0, 128)
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 28)


        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = 600
        self.rect.y = 450
# Сообщение кнопки создается только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""

        self.msg_image = self.font.render(msg, True, self.text_color,
                                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_easy(self):
        # Отображение пустой кнопки и вывод сообщения.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)