import pygame
import os


# ** Misc but essential variables **
creature_sprites = {
    "mango": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'manga_anime.png')),
    "cool ross": pygame.image.load(os.path.join(os.path.dirname(__file__), 'placeholder_images', 'ross_spritev.png')),
    "harold": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'harold.png')),
    "cool man": pygame.image.load(os.path.join(os.path.dirname(__file__), 'images', 'very_epic_image.png'))
}

# Tiles
tile_size = 100
walkable_dirt = pygame.image.load("tiles\\dirt.png")
nonwalkable_dirt = pygame.image.load("tiles\\dirt2.png")
background = walkable_dirt
tiles_group = pygame.sprite.Group()