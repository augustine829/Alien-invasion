#!/usr/bin/env python
# coding=utf-8


import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize one game and display one object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_hight))

    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")

    # set background color
    bg_color = (230, 230, 230)

    # game loop
    while True:
        gf.check_events(ship)
        ship.update()
        
        # file color
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # visualize the window
        pygame.display.flip()

run_game()
