import pygame
from pygame.locals import *
import os
import sys
import random
import pygame_gui
import gif_pygame
from pygame.sprite import Group
from main import creature_sprites


def creature_retriever(creature):
    for key in creature_sprites:
        if key == creature:
            return creature_sprites.get(key)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1

class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()