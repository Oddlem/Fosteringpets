import pygame
from pygame.locals import *
import os
import sys
import random
import pygame_gui
import gif_pygame
from pygame.sprite import Group


# Vital calls and variables for the game to run 
pygame.init()
pygame.display.set_caption("creature game")
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load(os.path.join(os.path.dirname(__file__), "placeholder_images", "background_test.png"))
pygame.key.set_repeat(True)
running = True


# ** Functions **
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
        pygame.draw.rect(surface, (0,0,0))


# ** Objects, sprites, and more **
creature_sprites = {
    "ross": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'ross2.png')), 
    "cool ross": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'ross_spritev.png')),
    "harold": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'harold.png'))
}

player_instance = Player(300, 400, pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'gif_test.gif')))
player_group = pygame.sprite.Group()
player_group.add(player_instance)
creature_group = pygame.sprite.Group()

harold = Creature(1000, 500, creature_retriever("harold"))
ross = Creature(1000, 900, creature_retriever("ross"))
creature_group.add(harold)

solid_objects = [
    player_instance,
    harold
]

# ** Game loop **
while running:
    screen.blit(background, (0,0))
    creature_group.update()
    creature_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                player_instance.rect.move_ip(-1,0)
            if event.key == K_RIGHT or event.key == K_d:
                player_instance.rect.move_ip(1,0)
            if event.key == K_DOWN or event.key == K_s:
                player_instance.rect.move_ip(0,1)
            if event.key == K_UP or event.key == K_w:
                player_instance.rect.move_ip(0,-1)
            for characters in solid_objects:
                if pygame.Rect.colliderect(player_instance.rect, harold.rect):
                    if event.key == K_LEFT or event.key == K_a:
                        player_instance.rect.move_ip(1,0)
                    if event.key == K_RIGHT or event.key == K_d:
                        player_instance.rect.move_ip(-1,0)
                    if event.key == K_DOWN or event.key == K_s:
                        player_instance.rect.move_ip(0,-1)
                    if event.key == K_UP or event.key == K_w:
                        player_instance.rect.move_ip(0,1)
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                player_instance.rect.move_ip(0,0)
            if event.key == K_RIGHT:
                player_instance.rect.move_ip(0,0)
            if event.key == K_DOWN:
                player_instance.rect.move_ip(0,0)
            if event.key == K_UP:
                player_instance.rect.move_ip(0,0)
        if event.type == pygame.K_e:
            pass
