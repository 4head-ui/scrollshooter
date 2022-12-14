class Settings():
    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1
        self.alien_points = 50


    def __init__(self):
        # Параметры экрана
        self.screen_width = 1300
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.bg_color1 = (255, 0, 0)
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
         # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.ship_limit = 3
        self.initialize_dynamic_settings()
        self.score_scale = 1.5




    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.speedup_scale = 1.1
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_direction *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

