#!/usr/bin/env python
# coding=utf-8

import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # initialize spaceship and itt locatio
        self.screen = screen.get_rect
        self.ai_settings = ai_settings
        self.moving_right = False

        # load ship image and draw rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put spaceship on the bottom of window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        # put the spaceship on specific location
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_right:
           self.rect.centerx += 1 


