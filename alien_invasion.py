#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Tian Chen
# @times: 2020/7/1  19:22
# @File: alien_invasion.py
# @email: chentianfighting@126.com
import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from Button import Button
import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_setting, screen, 'Play')
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_setting)
    # 创建一艘飞船
    ship = Ship(ai_setting, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一群外星人
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_setting, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_setting, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
        # 每次循环时都会重绘屏幕
        gf.update_screen(ai_setting, screen, stats, ship, aliens, bullets,
                         play_button)


run_game()