import pygame
from pygame.locals import *
import os
import random

pygame.init()
pygame.display.set_caption("weeeeeee")
screen = pygame.display.set_mode((1080, 720))
background = (100, 100, 100)
red = (200, 20, 20)

class Square(pygame.sprite.Sprite): 
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("very_epic_image.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

square = Square(500, 300)

print(square)

# running = True
# while running:
#     screen.fill(background)
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False
#         if event.type == MOUSEBUTTONDOWN:
#             pass
#         if event.type == KEYDOWN:
#             pass