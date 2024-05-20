import json
import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption("creature game")
screen = pygame.display.set_mode((1300, 800))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
pygame.key.set_repeat(True)

manager = pygame_gui.UIManager((1300, 800))

map_width = 8
map_height = 13
tile_size = 100

# This is here so that text can be looped through and placed in the dialogue box.
dialogue = {}
with open('dialogue.json') as file:
  dialogue = json.load(file)


running = True
character_can_move = True
show_dialogue_box = False

# Dialogue
dialogue_box = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((150, 500), (1000, 250)), 
                                             html_text = '<body style="black">test</body>', 
                                             manager = manager)
dialogue_box.hide()