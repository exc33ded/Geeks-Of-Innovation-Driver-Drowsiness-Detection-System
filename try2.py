import pygame
import subprocess
pygame.init()

# display
WIDTH = 1366
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Drowsiness Detector")

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
title_text = title_font.render("Drowsiness Alarm", True, text_color)
start_text = menu_font.render("Begin Drowsiness Detection", True, text_color)
options_text = menu_font.render("About", True, text_color)
quit_text = menu_font.render("Exit", True, text_color)

# Set up the text rectangles
title_rect = title_text.get_rect()
title_rect.center = (WIDTH // 2, HEIGHT // 4)
start_rect = pygame.Rect((WIDTH // 2) - 187, HEIGHT // 2, 375, 50)
options_rect = pygame.Rect((WIDTH // 2) - 75, (HEIGHT // 2) + 51, 150, 50)
quit_rect = pygame.Rect((WIDTH // 2) - 75, (HEIGHT // 2) + 102, 150, 50)

# Set up colors for rectangles
start_rect_color = bg_color
options_rect_color = bg_color
quit_rect_color = bg_color

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(mouse_pos):
                # Start game code here
                subprocess.run(["python", "start.py"])
            elif options_rect.collidepoint(mouse_pos):
                # Options code here
                subprocess.run(["python", "about.py"])
            elif quit_rect.collidepoint(mouse_pos):
                pygame.quit()
                quit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            start_rect_color = highlight_color if start_rect.collidepoint(mouse_pos) else bg_color
            start_text = menu_font.render("Begin Drowsiness Detection", True, text_color_reverse if start_rect.collidepoint(mouse_pos) else text_color)
            options_rect_color = highlight_color if options_rect.collidepoint(mouse_pos) else bg_color
            options_text = menu_font.render("About", True, text_color_reverse if options_rect.collidepoint(mouse_pos) else text_color)
            quit_rect_color = highlight_color if quit_rect.collidepoint(mouse_pos) else bg_color
            quit_text = menu_font.render("Exit", True, text_color_reverse if quit_rect.collidepoint(mouse_pos) else text_color)
    
    #Menu
    screen.fill(bg_color)
    screen.blit(title_text, title_rect)
    pygame.draw.rect(screen, start_rect_color, start_rect)
    pygame.draw.rect(screen, border_color, start_rect, 3)
    start_text_rect = start_text.get_rect(center=start_rect.center)
    screen.blit(start_text, start_text_rect)
    pygame.draw.rect(screen, options_rect_color, options_rect)
    pygame.draw.rect(screen, border_color, options_rect, 3)
    options_text_rect = options_text.get_rect(center=options_rect.center)
    screen.blit(options_text, options_text_rect)
    pygame.draw.rect(screen, quit_rect_color, quit_rect)
    pygame.draw.rect(screen, border_color, quit_rect, 3)
    quit_text_rect = quit_text.get_rect(center=quit_rect.center)
    screen.blit(quit_text, quit_text_rect)
    copyright = menu_font.render("Copyright © 2023 Geeks Of Innovation", True, text_color)
    copyright_rect = copyright.get_rect()
    copyright_rect.bottomright = (WIDTH-10, HEIGHT-10)
    screen.blit(copyright, copyright_rect)

    pygame.display.update()
