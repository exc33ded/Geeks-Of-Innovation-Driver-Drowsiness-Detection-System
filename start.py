import pygame
import subprocess
pygame.init()

# display
WIDTH = 1366
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Begin Drowsiness Detection")

# Set up the fonts
title_font = pygame.font.Font(None, 64)
menu_font = pygame.font.Font(None, 32)

# Set up the colors
bg_color = (0, 0, 0)  # black background
text_color = (255, 255, 255)  # white text
text_color_reverse = (0, 0, 0)  # text when highlighted
highlight_color = (255, 255, 255)  # white highlight
border_color = (100, 100, 100)  # dark gray border

# Set up the text
title_text = title_font.render("Loading..., Please wait!!!", True, text_color)

# Set up the text rectangles
title_rect = title_text.get_rect()
title_rect.center = (WIDTH // 2, HEIGHT // 4)

screen.fill(bg_color)
screen.blit(title_text, title_rect)
copyright = menu_font.render("Copyright © 2023 Geeks Of Innovation", True, text_color)
copyright_rect = copyright.get_rect()
copyright_rect.bottomright = (WIDTH-10, HEIGHT-10)
screen.blit(copyright, copyright_rect)

pygame.display.update()
subprocess.run(["python", "main.py"])
