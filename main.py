import pygame
import pygame_gui
import os
from pygame.locals import *
from pygame.sprite import Group
from tiles import *
from dialogue import *
from config import *
from assets import *
import config


# ** This function needs to be here **
def creature_retriever(creature):
    return creature_sprites.get(creature)


# ** Game States **
class Player_Cave():
    def __init__(self):
        pass


# ** Classes **
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Creature(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image, is_hurt):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.is_hurt = True
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Nonwalkable_tiles(pygame.sprite.DirtySprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# ** Objects, sprites, and more **

# Player
player_instance = Player(300, 400, pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'gif_test.gif')))
player_group = pygame.sprite.Group()
player_group.add(player_instance)

# Creatures
creature_group = pygame.sprite.Group()
harold = Creature("harold", 900, 500, creature_retriever("harold"), True)
mango = Creature("mango", 700, 300, creature_retriever("mango"), True)
creature_group.add(harold, mango)

solid_objects = [
    harold,
    mango
]

creature_rects = [creature.rect for creature in creature_group]

# **Tile Collision **
colliding_tiles = pygame.sprite.spritecollide(player_instance, tiles_group, False)


# ** Functions **
def draw_background(screen, image, rows, columns, non_walkable_group):
    for y in range(rows):
        for x in range(columns):
            screen.blit(image, (x * tile_size, y * tile_size))
    for tile in non_walkable_group:
        screen.blit(tile.image, tile.rect)

# def generate_room(group, x, y, width, height, tile_size, tile_image):
#     for y in range(y, y + height):
#         for x in range(x, x + height):
#             if y == y or y == y + height - 1 or x == x + width - 1:
#                 tile = Nonwalkable_tiles(tile_image)
#                 tile.rect.x = x * tile_size
#                 tile.rect.y = y * tile_size
#                 group.add(tile)

# Calculates distance between two objects' rects
def distance_rects(rect1, rect2):
    return ((rect1.x - rect2.x) ** 2 + (rect1.y - rect2.y) ** 2) ** 0.5

# Returns the first creature within a threshold 
def get_creature_within_threshold(player, creatures, threshold):
    for creature in creatures:
        distance = distance_rects(player, creature.rect)
        if distance < threshold:
            return creature

    return None 

# def offscreen_check():
#     if player_instance.rect.x > 0 and player_instance.y > 0:
#         config.character_can_move = False

def dialogue_box_trigger(event):
    if event.type == pygame.KEYUP and event.key == pygame.K_e:
        creature = get_creature_within_threshold(player_instance.rect, creature_group, 200)
        if creature != None:
            config.show_dialogue_box = not config.show_dialogue_box
            config.character_can_move = not config.character_can_move
            if (config.show_dialogue_box):
                name = creature.name
                text = config.dialogue[name]

                dialogue_box.html_text = text
                dialogue_box.rebuild()
                dialogue_box.show()
            else:
                dialogue_box.hide()