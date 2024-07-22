import pygame
import os


# reminder: when I have the chance, I need to clean this up lol
# Creatures
creature_sprites = {
    "mango": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'manga_anime.png')),
    "harold": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'harold.png')),
    "dringus": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'dringus.png'))
}

# Objects
object_sprites = {
    "M_potion": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'water_potion.png')),
    "m_bed": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'goblin_bed.png')),
    "end_table": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'end_table.png')),
}

# nonwalkable_dirt = pygame.image.load("tiles\\dirt2.png")
background = pygame.image.load("tiles\\dirt.png")