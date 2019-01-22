import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建游戏屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")  # 设置标题内容
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "PLAY")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船，一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    # 创建外星人实例
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标的事件
        # gf.check_events(ship)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # 每次循环时都重新绘制屏幕
        # gf.update_screen(ai_settings, screen, ship)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
