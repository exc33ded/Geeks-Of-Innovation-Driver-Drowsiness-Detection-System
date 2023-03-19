import pygame

pygame.init()

# Define constants for the display and fonts
DISPLAY_WIDTH = 1366
DISPLAY_HEIGHT = 768
FONT_SIZE_TITLE = 64
FONT_SIZE_BODY = 32

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Create the display and set the caption
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("About Page")

# Create the font objects
title_font = pygame.font.Font(None, 64)
body_font = pygame.font.Font(None, 32)

# Define the text content
title_text = "About This Project"
body_text = ["Drowsiness detection software is a tool that can help prevent accidents on the road.",
             "It uses computer vision and machine learning algorithms to analyze the driver's eyes and detect signs of fatigue.",
             "If drowsiness is detected, the software can alert the driver with an alarm or other notification.",
             "By helping drivers stay alert, drowsiness detection software can help reduce the risk of accidents caused by fatigue.",
             "                             Geeks Of Innovation Team Members:-",
             " ",
             "                                       Mohammed Sarim",
             "                                     S.M. Talha Husain",
             "                                     S.M. Hamza Husain",
             "                                      Khushnood Bilal"]

# Render the text surfaces
title_surface = title_font.render(title_text, True, WHITE)
body_surfaces = [body_font.render(line, True, WHITE) for line in body_text]

# Calculate the height of the body text based on the number of lines and font size
body_height = len(body_surfaces) * body_font.get_height()

# Define the positions of the text surfaces
title_position = ((DISPLAY_WIDTH - title_surface.get_width()) // 2, DISPLAY_HEIGHT // 4)
body_position = ((DISPLAY_WIDTH - max([s.get_width() for s in body_surfaces])) // 2,
                 DISPLAY_HEIGHT // 2 - body_height // 2)

# Create the background surface and blit the text surfaces onto it
background = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
background.fill(BLACK)
background.blit(title_surface, title_position)
for i, surface in enumerate(body_surfaces):
    position = (body_position[0], body_position[1] + i * body_font.get_height())
    background.blit(surface, position)

# Create the main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background onto the display
    display.blit(background, (0, 0))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
