import pygame
import pygame_gui
import os
from pygame.locals import *
from pygame.sprite import Group
from tiles import *
from config import *
from assets import *
import config
import assets
import time


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
# Next, I need to make player states
        self.elapsed = 0
        self.image = image
        self.rect = Rect(200, 200, 90, 90)
        self.rect.center = (x, y)
        self.frames = []
        # self.walking_up = []
        # self.walking_left = []
        # self.walking_down = []
        # self.walking_right = []


# refactor this, either putting all this in tiles or putting the movement function in HERE
        self.current_sprite = 0
        self.frames.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'frame1.png')).convert_alpha())
        self.frames.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'frame2.png')).convert_alpha())
        self.frames.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'frame3.png')).convert_alpha())
        self.frames.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'frame4.png')).convert_alpha())

        # self.walking_up.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'walking', 'walk_up.png')).convert_alpha())
        # self.walking_left.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'walking', 'walk_left.png')).convert_alpha())
        # self.walking_down.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'walking', 'walk_down.png')).convert_alpha())
        # self.walking_right.append(pygame.image.load(os.path.join(os.path.dirname(__file__), 'walking', 'walk_right.png')).convert_alpha())
        
# A copy of animate() so I can de-hardcode it 
    # def animate(self, surface, images):
    #     if config.character_can_move:
    #         surface.blit(images[self.current_sprite], self.rect)
    #     else:
    #         surface.blit(self.images[0], self.rect)

    def animate(self, surface):
        if config.character_can_move:
            surface.blit(self.frames[self.current_sprite], self.rect)
        else:
            surface.blit(self.frames[0], self.rect)
    
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.elapsed > 250:
            self.elapsed = current_time
            self.current_sprite = (self.current_sprite + 1) % len(self.frames)
        self.image = self.frames[self.current_sprite]



class Creature(pygame.sprite.Sprite):
    def __init__(self, name, x, y, size_x, size_y, image):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = Rect(x, y, size_x, size_y)
        self.rect.center = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Object(pygame.sprite.Sprite):
    def __init__(self, name, x, y, size_x, size_y, image):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = Rect(x, y, size_x, size_y)
        self.rect.center = (x, y)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Items you can store in your inventory; these are different from objects that you just interact with
class Item(pygame.sprite.Sprite):
    def __init__(self, name, x, y, size_x, size_y, image):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = Rect(x, y, size_x, size_y)
        self.rect.center = (x, y)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        

# ** Objects, sprites, and more **

# Player
player_instance = Player(300, 400, None)
player_group = pygame.sprite.Group()
player_group.add(player_instance)

# Creatures
creature_group = pygame.sprite.Group()
harold = Creature("harold", 900, 600, 120, 90, image_retriever(creature_sprites, "harold"))
mango = Creature("mango", 700, 300, 90, 90, image_retriever(creature_sprites, "mango"))
dringus = Creature("dringus", 400, 200, 90, 90, image_retriever(creature_sprites, "dringus"))
# I'm keeping it so you can walk through dringus cause I thought it was funny :)
creature_group.add(harold, mango, dringus)

# Objects
object_group = pygame.sprite.Group()
# end_table = Object("end_table", 700, 150, pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'end_table.png')))
mysterious_potion = Object("m_potion", 700, 125, 45, 45, image_retriever(object_sprites, "M_potion"))
m_bed = Object("m_bed", 900, 150, 95, 95, image_retriever(object_sprites, "m_bed"))
object_group.add(mysterious_potion, m_bed)

solid_objects = [
    harold,
    mango,
    mysterious_potion,
    m_bed
]

# def state_machine(state):
#     if state == cave:
#         pass
#     if state == hub:
#         pass
#     if state == title_screen:
#         pass


# * reminder to redo all of this with tiled LOL 
def draw_tiles(screen, rows, columns):
    for y in range(rows):
        for x in range(columns):
            key = tilemap_cave[y][x]
            image = cave_textures[key]
            screen.blit(image, (x * tile_size, y * tile_size))


# Calculates distance between two objects' rects
def distance_rects(rect1, rect2):
    return ((rect1.x - rect2.x) ** 2 + (rect1.y - rect2.y) ** 2) ** 0.5


# Returns the first creature within a threshold 
def get_thing(player, thingies, threshold):
    for thing in thingies:
        distance = distance_rects(player, thing.rect)
        if distance < threshold:
            return thing
    return None 


def load_text(name, file):
    content = {}
    with open(name) as file:
        content = json.load(file)
        return content


def dialogue_box_trigger(event):
    if event.type == pygame.KEYUP and event.key == pygame.K_e:
        creature = get_thing(player_instance.rect, creature_group, 125)
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


# Add a check for whichever object is the closest, and you return THAT
def text_box_trigger(event):
    if event.type == pygame.KEYUP and event.key == pygame.K_e:
        object = get_thing(player_instance.rect, object_group, 125)
        if object != None:
            config.show_dialogue_box = not config.show_dialogue_box
            config.character_can_move = not config.character_can_move
            if (config.show_dialogue_box):
                name = object.name
                text = config.text[name]

                dialogue_box.html_text = text
                dialogue_box.rebuild()
                dialogue_box.show()
            else:
                dialogue_box.hide()

# modify it to where it tracks the last movement and use THAT to trigger the dialogue box to show up
def box_trigger(event):
    if event.type == pygame.KEYUP and event.key == pygame.K_e:
        thing = get_thing(player_instance.rect, )

# next time I'll fix the objects, and I'll also separate items and objects in order to be able to add items to the player's inventory later on

# I also wanna make it so that in order for e to activate, you have to be facing towards something. This will be after I make and add sprites for each direction

# **Biggest priority until next repo: Refactor everything. I got a lot done, now's the time to clean it up