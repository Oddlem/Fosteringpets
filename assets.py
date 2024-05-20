import pygame
import os


# Creatures
creature_sprites = {
    "mango": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'manga_anime.png')),
    "cool ross": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'ross_spritev.png')),
    "harold": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'harold.png')),
    "cool man": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'very_epic_image.png'))
}

# Objects
object_sprites = {
    "M_potion": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'water_potion.png')),
}

# nonwalkable_dirt = pygame.image.load("tiles\\dirt2.png")
background = pygame.image.load("tiles\\dirt.png")