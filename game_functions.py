#!/usr/bin/env python
# coding=utf-8

import sys
import pygame


def check_keydown_events(self, ship):
    if event.key == pygame.K_RIGHT:
        # moving right
        ship.moving_right = True
        # moving left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(self, ship):
    if event.key == pygame.K_RIGHT:
        # moving right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    # respone to keyboard and mouse feedback event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



