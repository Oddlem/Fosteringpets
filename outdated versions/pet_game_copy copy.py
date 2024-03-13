import pygame
from pygame.locals import *
import os
import sys
import random
import pygame_gui
import gif_pygame
from pygame.sprite import Group
# from utility import creature_retriever

# There's four things to do right now:

# 1. Figure out how to animate sprites
# 2. Modualize this file and organize everything
# 3. Properly implement objects, and have classes grab an image from a list rather than be hardcoded ** IN PROGRESS **
# 4. Find a way to implement collision in the background, maybe even by adding wall sprites
# 5. Turn some things into functions and overall make the game loop itself more clean


# Things to do after I finish these:

# 1. Figure out how to make different creature objects from the Creature class, AND animate them
# 2. Find a way to create different screens/scenes, though I have a small idea already of how to do that
# 3. Interacting with creatures, each with unique dialogue. It's vital to modualize BEFORE this step
# 4. Have unique animations for each action and EACH character, like walking, idling, talking, etc.
# 5. Create a working GUI with buttons, though a mockup before this is important


# Vital calls and variables for the game to run 
pygame.init()
pygame.display.set_caption("harold")
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
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Gif_test.gif")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1

class Creature(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# ** Objects, sprites, and more **
player_instance = Player(300, 400)
player_group = pygame.sprite.Group()
player_group.add(player_instance)

creature_sprites = {
    "ross": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'ross2.png')), 
    "cool ross": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'ross_spritev.png')),
    "harold": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'harold.png'))
}    

harold = Creature(1000, 500, creature_retriever("harold"))
ross = Creature(1000, 900, creature_retriever("ross"))
creature_group = pygame.sprite.Group()
creature_group.add(harold)

solid_objects = [
    player_instance.rect,
    harold.rect,
    ross.rect
]

while running:
    screen.blit(background, (0,0))
    player_group.update()
    player_group.draw(screen)
    creature_group.update()
    creature_group.draw(screen)
    # for creature in creature_group:
    #     creature.update()
    #     creature.draw(screen)
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
                if pygame.Rect.colliderect(player_instance.rect, creature_group.rect):
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
