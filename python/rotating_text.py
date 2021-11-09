import pygame

pygame.init() 

WHITE = (255, 255, 255)
BORDER = (51, 113, 140)
FONT_COLOUR = (185, 146, 143)

PI = 3.141592653

# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rotating text test")

# loop until user clicks X button 
done = False 
clock = pygame.time.Clock()

text_rotate_degrees = 0 

# loop as long as done == False
while not done:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)

    # borders
    pygame.draw.line(screen, BORDER, [100, 50], [200, 50])
    pygame.draw.line(screen, BORDER, [100, 50], [100, 150])

    # select font, size, bold, italics
    font = pygame.font.SysFont('Verdana', 25, True, True) 

    # sideways text 
    text = font.render("Sideways text :D", True, FONT_COLOUR)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [0, 0])

    #flipped text
    text = font.render("Flipped text", True, FONT_COLOUR)
    text = pygame.transform.flip(text, False, True) 
    screen.blit(text, [30, 20])

    # animated rotation
    text = font.render("rotating text", True, FONT_COLOUR)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 1
    screen.blit(text, [100, 50])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()