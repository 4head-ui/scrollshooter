import os
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from easy import Easy
from medium import Medium
from hard import Hard
from scoreboard import Scoreboard

class AlienInvasion:
    #Класс для управления ресурсами и поведением игры.


    def __init__(self):
        #Инициализирует игру и создает игровые ресурсы.
        pygame.init()
        pygame.display.set_caption("Anti-creep")
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        self.button = Easy(self, "Easy")
        self.button1 = Medium(self,'Medium')
        self.button2 = Hard(self,'Hard')
        self.sb = Scoreboard(self)
        self.sound = pygame.mixer.Sound('sound/nomnom.wav')

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_screen()
                self._update_bullets()
                self.ship.update()
                self._update_aliens()
            self._update_screen()


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
           self._ship_hit()
        self._check_aliens_bottom()

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.25)
        elif self.stats.ships_left == 0:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():

            if alien.rect.bottom >= screen_rect.bottom:

                self._ship_hit()
                break



    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_bullets(self):
        self.bullets.update()
        # Уничтожение исчезнувших снарядов.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
                self.sound.play()
        if not self.aliens:
            self.settings.increase_speed()
            self.bullets.empty()
            self._create_fleet()
            self.stats.level += 1
            self.sb.prep_level()



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
                 self.play(mouse_pos)
                 self.easy(mouse_pos)
                 self.medium(mouse_pos)
                 self.hard(mouse_pos)

    def _check_play_button(self):
        """Запускает новую игру при нажатии кнопки Play."""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()
        self.ship.center_ship()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        pygame.mouse.set_visible(False)

    def play(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._check_play_button()

    def easy(self, mouse_pos):
        button_clicked1 = self.button.rect.collidepoint(mouse_pos)
        if button_clicked1 and not self.stats.game_active:
            self._check_play_button()
            self.settings.fleet_direction = 1


    def medium(self, mouse_pos):
        button_clicked2 = self.button1.rect.collidepoint(mouse_pos)
        if button_clicked2 and not self.stats.game_active:
            self._check_play_button()
            self.settings.fleet_direction = 2


    def hard(self, mouse_pos):
        button_clicked3 = self.button2.rect.collidepoint(mouse_pos)
        if button_clicked3 and not self.stats.game_active:
            self._check_play_button()
            self.settings.fleet_direction = 3




    def _check_keydown_events(self, event):
        if event.key == pygame.K_p:
            self.stats.game_active = True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.sb.show_score()
        # Отображение последнего про рисованного экрана.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if self.stats.game_active == False:
            self.play_button.draw_button()
            self.button.draw_easy()
            self.button1.draw_medium()
            self.button2.draw_hard()
        pygame.display.flip()


if __name__ == '__main__':
# Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()