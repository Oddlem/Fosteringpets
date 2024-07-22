import pygame
from pygame.locals import *
from pygame.sprite import Group
from tiles import *
from main import *
from config import *
from assets import *

# Essential for the game loop; allows the player to move
def character_movement():
    if not config.character_can_move:
        return
    if event.key == K_LEFT or event.key == K_a:
        player_instance.rect.move_ip(-1,0)
    if event.key == K_RIGHT or event.key == K_d:
        player_instance.rect.move_ip(1,0)
    if event.key == K_DOWN or event.key == K_s:
        player_instance.rect.move_ip(0,1)
    if event.key == K_UP or event.key == K_w:
        player_instance.rect.move_ip(0,-1)

while config.running:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE:
            config.running = False
        manager.process_events(event)
        dialogue_box_trigger(event)
        text_box_trigger(event)
        if event.type == pygame.KEYDOWN:
            character_movement()
            for thing in solid_objects:
                if pygame.Rect.colliderect(player_instance.rect, thing.rect):
                    if event.key == K_LEFT or event.key == K_a:
                        player_instance.rect.move_ip(1,0)
                    if event.key == K_RIGHT or event.key == K_d:
                        player_instance.rect.move_ip(-1,0)
                    if event.key == K_DOWN or event.key == K_s:
                        player_instance.rect.move_ip(0,-1)
                    if event.key == K_UP or event.key == K_w:
                        player_instance.rect.move_ip(0,1)
            # for tile in cave_textures:
            #     if pygame.Rect.colliderect(tile[3].rect, player_instance.rect):
            #         if event.key == K_LEFT or event.key == K_a:
            #             player_instance.rect.move_ip(1,0)
            #         if event.key == K_RIGHT or event.key == K_d:
            #             player_instance.rect.move_ip(-1,0)
            #         if event.key == K_DOWN or event.key == K_s:
            #             player_instance.rect.move_ip(0,-1)
            #         if event.key == K_UP or event.key == K_w:
            #             player_instance.rect.move_ip(0,1)

    creature_group.update()
    object_group.update()
    manager.update(dt)

    draw_tiles(screen, 8, 13)
    
    creature_group.draw(screen)
    object_group.draw(screen)

    player_instance.animate(screen)
    player_instance.update()
# A temporary fix until I add collision to tiles; disallows the player from moving outside the screen
    player_instance.rect.clamp_ip(screen_rect)
    manager.draw_ui(screen)
    pygame.display.update()