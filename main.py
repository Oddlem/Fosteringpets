import pygame
from pygame.locals import *
import os
import sys
import random
import pygame_gui
import gif_pygame
from pygame.sprite import Group
from tiles import *


# Vital calls and variables for the game to run 
pygame.init()
pygame.display.set_caption("creature game")
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock
background = pygame.image.load(os.path.join(os.path.dirname(__file__), "placeholder_images", "background_test.png"))
pygame.key.set_repeat(True)
running = True


# ** This function needs to be here **
def creature_retriever(creature):
    for key in creature_sprites:
        if key == creature:
            return creature_sprites.get(key)


# ** Classes **
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


# ** Objects, sprites, and more **
creature_sprites = {
    "mango": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'manga_anime.png')), 
    "cool ross": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'ross_spritev.png')),
    "harold": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'harold.png')),
    "cool man": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'very_epic_image.png'))
}

player_instance = Player(300, 400, pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'gif_test.gif')))
player_group = pygame.sprite.Group()
player_group.add(player_instance)

creature_group = pygame.sprite.Group()
harold = Creature(900, 500, creature_retriever("harold"))
ross = Creature(700, 300, creature_retriever("mango"))

creature_group.add(harold, ross)

solid_objects = [
    harold,
    ross
]


# ** Functions **
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

def fps_meter():
    clock.tick()


# ** Game loop **
while running:
    screen.blit(background, (0,0))
    harold.update()
    harold.draw(screen)
    ross.update()
    ross.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            character_movement_true()
            for characters in solid_objects:
                if pygame.Rect.colliderect(player_instance.rect, characters):
                    if event.key == K_LEFT or event.key == K_a:
                        player_instance.rect.move_ip(1,0)
                    if event.key == K_RIGHT or event.key == K_d:
                        player_instance.rect.move_ip(-1,0)
                    if event.key == K_DOWN or event.key == K_s:
                        player_instance.rect.move_ip(0,-1)
                    if event.key == K_UP or event.key == K_w:
                        player_instance.rect.move_ip(0,1)
        if event.type == pygame.KEYUP:
            character_movement_false()
        if event.type == pygame.K_e:
            pass