import pygame
import pygame_gui
import os
from pygame.locals import *
from pygame.sprite import Group
from tiles import *
from config import *
from assets import *
import config


# ** This function needs to be here **
def image_retriever(group, image):
    return group.get(image)

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
    def __init__(self, name, x, y, image):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Object(pygame.sprite.Sprite):
    def __init__(self, name, x, y, image):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ** Objects, sprites, and more **

# Player
player_group = pygame.sprite.Group()
player_instance = Player(300, 400, pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'gif_test.gif')))
player_group.add(player_instance)

# Creatures
creature_group = pygame.sprite.Group()
harold = Creature("harold", 900, 500, image_retriever(creature_sprites, "harold"))
mango = Creature("mango", 700, 300, image_retriever(creature_sprites, "mango"))
creature_group.add(harold, mango)

# Objects
# object_group = pygame.sprite.Group()
# mysterious_potion = Object("mysterious_potion", 500, 300, image_retriever(object_sprites, "m_potion"))
# object_group.add(mysterious_potion)

solid_objects = [
    harold,
    mango
]

creature_rects = [creature.rect for creature in creature_group]


# ** Functions **
def draw_background(screen, image, rows, columns):
    for y in range(rows):
        for x in range(columns):
            screen.blit(image, (x * tile_size, y * tile_size))

def draw_tiles(x, y, ):
    pass

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

# Rework this function to where it ALSO checks for an object. If that returns true, the object is added to the player's inventory.