import pygame.font



class Scoreboard():

    """Класс для вывода игровой информации."""



    def __init__(self, ai_game):

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats


    # Настройки шрифта для вывода счета.


        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
# Подготовка исходного изображения.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                    self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20



    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)

# Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top



    def check_high_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            with open ('highscore.txt','w')as f:
                f.write (str(self.stats.score))


        self.prep_high_score()


    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        level_str = str(self.stats.level)

        self.level_image = self.font.render(level_str, True,
        self.text_color, self.settings.bg_color)

    # Уровень выводится под текущим счетом.
        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        ship_str = str(self.stats.ships_left)

        self.ship1_image = self.font.render(ship_str, True,
            self.text_color, self.settings.bg_color)

        # Уровень выводится под текущим счетом.
        self.ship1_rect = self.ship1_image.get_rect()

        self.ship1_rect.topleft = self.screen_rect.topleft
        self.ship1_rect.x +=10







    def show_score(self):
        """Выводит счет на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ship1_image, self.ship1_rect)

