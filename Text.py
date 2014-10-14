# 2014-06-11 ( eshagdar )

import pygame

def text_to_screen(screen, text, x, y, size = 15,
            color = (255, 255, 255), font_type = 'ArialNarrow'):
    try:
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception, e:
        print 'Font Error, saw it coming'
        raise e