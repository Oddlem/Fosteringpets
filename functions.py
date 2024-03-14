import pygame
from pygame.locals import *
import os
import sys
import random
from main import *

from pygame.sprite import Group

# This contains essential functions as a way to better organize the main file


# Functions:

def character_movement_true():
    if event.key == K_LEFT or event.key == K_a:
        player_instance.rect.move_ip(-1,0)
    if event.key == K_RIGHT or event.key == K_d:
        player_instance.rect.move_ip(1,0)
    if event.key == K_DOWN or event.key == K_s:
        player_instance.rect.move_ip(0,1)
    if event.key == K_UP or event.key == K_w:
        player_instance.rect.move_ip(0,-1)

def character_movement_false():
    if event.key == K_LEFT or event.key == K_a:
        player_instance.rect.move_ip(0,0)
    if event.key == K_RIGHT or event.key == K_d:
        player_instance.rect.move_ip(0,0)
    if event.key == K_DOWN or event.key == K_s:
        player_instance.rect.move_ip(0,0)
    if event.key == K_UP or event.key == K_w:
        player_instance.rect.move_ip(0,0)
        

# ***** WILL RETURN TO THIS WHEN I FINISH MODUALIZING *****
# def get_sprites(sprite):
#     for sprite in Group():
#         return sprite

def sprite_loader():
    pass
# frame1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "placeholder_images", "frame1.png")),
# frame2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "placeholder_images", "frame2.png")),
# frame3 = pygame.image.load(os.path.join(os.path.dirname(__file__), "placeholder_images", "frame3.png")),
# frame4 = pygame.image.load(os.path.join(os.path.dirname(__file__), "placeholder_images", "frame4.png")),  

# player_idle_frames = [frame1, frame2, frame3, frame4]


# Lists:

