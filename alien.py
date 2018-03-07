# -*- coding:UTF-8-*-
import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    #初始化游戏
    pygame.init()
    ai_settings=Settings()
    #绘制屏幕
    screen=pygame.display.set_mode((ai_settings.screen_width,
                                    ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship=Ship(ai_settings,screen)

    #开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)



run_game()