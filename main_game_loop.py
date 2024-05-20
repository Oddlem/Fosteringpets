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
    dt = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE:
            config.running = False
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

    draw_background(screen, background, 8, 13)
    harold.draw(screen)
    mango.draw(screen)
    player_group.draw(screen)
    player_instance.rect.clamp_ip(screen_rect)
    manager.draw_ui(screen)
    pygame.display.update()