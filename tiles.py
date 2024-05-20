import pygame
from pygame.locals import *
import os
import sys
from pygame.sprite import Group

cave_textures = {
    0: pygame.image.load("tiles\\dirt.png"),
    2: pygame.image.load("tiles\\dirty_grass.png"),
    3: pygame.image.load("tiles\\dirt2.png"),
}

# Testing out different ways to make tilemaps
tilemap_cave = [

]

tilemap_cave = [
    [0,2,0,0,2,0,0,0],
    [0,0,0,0,0,0,0,2],
    [2,0,0,2,0,0,0,0],
    [0,0,0,0,0,2,0,0],
    [0,2,0,0,0,0,0,0]
]