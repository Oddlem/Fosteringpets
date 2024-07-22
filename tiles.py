import pygame
from pygame.locals import *
from pygame.sprite import Group

cave_textures = {
    0: pygame.image.load("tiles\\dirt.png"),
    2: pygame.image.load("tiles\\dirty_grass.png"),
    3: pygame.image.load("tiles\\dirt2.png"),
    4: pygame.image.load("tiles\\water1.png"),
    5: pygame.image.load("tiles\\water2.png"),
    6: pygame.image.load("tiles\\water3.png"),
    7: pygame.image.load("tiles\\water4.png"),
    8: pygame.image.load("tiles\\water32.png"),
    9: pygame.image.load("tiles\\water25.png"),
    10: pygame.image.load("tiles\\water34.png"),
    11: pygame.image.load("tiles\\water45.png"),
    12: pygame.image.load("tiles\\light_dirt.png"),
    13: pygame.image.load("tiles\\light_dirt_kinda.png"),
}


tilemap_cave = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,3,3,10,8,0,0,2,0,0,3,3,3],
    [3,3,0,11,9,0,0,0,0,0,2,3,3],
    [3,0,0,0,0,2,0,0,2,0,0,0,3],
    [3,2,0,0,2,0,0,0,0,0,0,2,3],
    [3,3,0,0,0,0,0,2,0,0,0,3,3],
    [3,3,3,2,0,0,13,0,0,0,3,3,3],
    [3,3,3,3,3,3,12,3,3,3,3,3,3],
]