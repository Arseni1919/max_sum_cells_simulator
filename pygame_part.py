from CONSTANTS import *


def update_sprites_with_new_positions(all_sprites, new_positions):
    for sprite in all_sprites:
        if sprite.name in new_positions:
            new_pos = new_positions[sprite.name]
            sprite.set_pos(new_pos)


def blit_pygame(screen, all_sprites, new_positions):
    update_sprites_with_new_positions(all_sprites, new_positions)
    all_arrived = False
    while not all_arrived:
        screen.fill(SKY_COLOR)

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Update the display
        pygame.display.flip()
        time.sleep(0.5)
        all_arrived = True
