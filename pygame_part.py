from CONSTANTS import *


def blit_pygame(screen, all_sprites):
    all_arrived = False
    while not all_arrived:
        screen.fill(SKY_COLOR)

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Update the display
        pygame.display.flip()
        all_arrived = True
