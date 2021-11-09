# http://programarcadegames.com/python_examples/f.php?file=simple_graphics_demo.py

import pygame

pygame.init() 

UGH = (179, 222, 228)
NEW = (235, 113, 108)
#26, 143, 61
COLOUR = (11, 192, 143)
#15, 113, 62
RRR = (218, 209, 45)
CCC = (122, 49, 167)
TTT = (127, 74, 215)
TE = (15, 71, 122)

PI = 3.141592653

# size of screen
size = (400, 500)
screen = pygame.display.set_mode(size)

# title
pygame.display.set_caption("blah blah")

# loop until user clicks close button- necessary
done = False
clock = pygame.time.Clock()

# loop while done == False
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
            # if user clicks close button

    #clear screen and fill ()
    screen.fill(UGH)

    # draw line at (surface, colour, from (0, 0) to (100, 100) and 5 pixels wide)
    pygame.draw.line(screen, COLOUR, [0,0], [100, 100], 5)

     # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, NEW, [0, 10 + y_offset], [100, 110 + y_offset], 5)

    #draw a rectangle - surface, colour, rect, width
    pygame.draw.rect(screen, RRR, [20, 20, 250, 100], 2)

    #draw an ellipse - surface, colour, rect, width
    pygame.draw.ellipse(screen, CCC, [20, 20, 250, 100], 2)

    #This draws a triangle using the polygon command
    pygame.draw.polygon(screen, TTT, [[100, 100], [0, 200], [200, 200]], 5)

    # font, size, bold, italics
    font = pygame.font.SysFont('Georgia', 30, False, True)
    # render text
    text = font.render("Hello world :)", True, TE)
    # put the text on the sxcreen
    screen.blit(text, [200, 450])

    # VITAL command line to update canvas with new drawing commands
    pygame.display.flip()
    # only loops max 60 times per second
    clock.tick(60)
# "always call this function" - the opposite of pygame.init()
pygame.quit()