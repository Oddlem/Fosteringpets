import pygame
from pygame.locals import *
import os
import sys
import random
import tkinter
from tkinter import filedialog
from tkinter import *

pygame.init()
pygame.display.set_caption("testin!!")
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load(os.path.join("Ross.png"))



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("very_epic_image.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5


    # def player_move(self, x, y):
    #     key = pygame.key.get_pressed()
    #     if key[pygame.K_RIGHT]:
    #         self.rect.x += x
    #     if key[pygame.K_UP]:
    #         self.rect.y -= y
    #     elif key[pygame.K_LEFT]:
    #         self.rect.x -= x
    #     elif key[pygame.K_DOWN]:
    #         self.rect.y += y

player_instance = Player(50, 50)
player_group = pygame.sprite.Group()
player_group.add(player_instance)

running = True
while running:
    screen.blit(background, (0,0))
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass