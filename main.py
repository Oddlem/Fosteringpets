import pygame
import pygame_gui
import os
import random

from pygame.locals import *
from pygame.sprite import Group
from tiles import *
from dialogue import *


# Vital calls and variables for the game to run
pygame.init()
pygame.display.set_caption("creature game")
screen = pygame.display.set_mode((1300, 800))
clock = pygame.time.Clock()
pygame.key.set_repeat(True)

running = True
character_can_move = True
show_dialogue_box = False
manager = pygame_gui.UIManager((1300, 800))

# ** Tiles **
tile_size = 100


# ** This function needs to be here **
def creature_retriever(creature):
    return creature_sprites.get(creature)


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

class Nonwalkable_tiles(pygame.sprite.DirtySprite):
    def __init__(self, image):
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

# Player
player_instance = Player(300, 400, pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'gif_test.gif')))
player_group = pygame.sprite.Group()
player_group.add(player_instance)

# Creatures
creature_group = pygame.sprite.Group()
harold = Creature(900, 500, creature_retriever("harold"))
mango = Creature(700, 300, creature_retriever("mango"))
creature_group.add(harold, mango)

# Tiles
walkable_dirt = pygame.image.load("tiles\\dirt.png")
nonwalkable_dirt = pygame.image.load("tiles\\dirt2.png")
background = walkable_dirt
bad_tiles_group = pygame.sprite.Group()

solid_objects = [
    harold,
    mango
]

# Dialogue

dialogue_box = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((150, 500), (1000, 250)), html_text = '<body text="black">Test</body>', manager = manager)
dialogue_box.hide()

# **Tile Collision **
colliding_tiles = pygame.sprite.spritecollide(player_instance, bad_tiles_group, False)


# ** Functions **
def character_movement():
    if not character_can_move:
        return
    if event.key == K_LEFT or event.key == K_a:
        player_instance.rect.move_ip(-1,0)
    if event.key == K_RIGHT or event.key == K_d:
        player_instance.rect.move_ip(1,0)
    if event.key == K_DOWN or event.key == K_s:
        player_instance.rect.move_ip(0,1)
    if event.key == K_UP or event.key == K_w:
        player_instance.rect.move_ip(0,-1)

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

# Next time!
def find_distance():
    pass

def dialogue_box_trigger(event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_e:
            global show_dialogue_box
            global character_can_move
            show_dialogue_box = not show_dialogue_box
            character_can_move = not character_can_move
            if (show_dialogue_box):
                dialogue_box.show()
            else:
                dialogue_box.hide()

# ** Game loop **
while running:
    dt = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE:
            running = False
        manager.process_events(event)
        dialogue_box_trigger(event)
        if event.type == pygame.KEYDOWN:
            character_movement()
            for character in solid_objects:
                if pygame.Rect.colliderect(player_instance.rect, character.rect):
                    if event.key == K_LEFT or event.key == K_a:
                        player_instance.rect.move_ip(1,0)
                    if event.key == K_RIGHT or event.key == K_d:
                        player_instance.rect.move_ip(-1,0)
                    if event.key == K_DOWN or event.key == K_s:
                        player_instance.rect.move_ip(0,-1)
                    if event.key == K_UP or event.key == K_w:
                        player_instance.rect.move_ip(0,1)

    player_group.update()
    harold.update()
    mango.update()
    manager.update(dt)

    draw_background(screen, background, 8, 13, bad_tiles_group)
    harold.draw(screen)
    mango.draw(screen)
    player_group.draw(screen)
    manager.draw_ui(screen)
    pygame.display.update()


# Dialogue logic:
    
# Checks if player is within a specific range of a creature, most likely by subtracting the distance between rects
# If this is true, a dialogue box will show on the screen