


class GameStats():


    def __init__(self, ai_game):
        self.game_active = False
        self.settings = ai_game.settings
        self.reset_stats()
        with open('highscore.txt', 'r')as f:
            d = f.read()
            c = int(d)
        self.high_score = c








    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1