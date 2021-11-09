# multiple random balls bouncing - space bar spawns more balls

import pygame
import random

# colours
FIRST_COLOUR = (7, 80, 162)
R = (random.randint(0, 255))
G = (random.randint(0, 255))
B = (random.randint(0, 255))
RANDOM_COLOUR = (R, G, B)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25

class Ball:
    #location and vector
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

def make_ball():
    ball = Ball()
    # starting position, take into account ball size
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    # speed and direction 
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)

    return ball

def main():

    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Balls")

    done = False
    clock = pygame.time.Clock()

    ball_list = []

    ball = make_ball()
    ball_list.append(ball)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)

        for ball in ball_list:
            # move ball's centre
            ball.x += ball.change_x
            ball.y += ball.change_y

            # bounce if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1

        # drawing
        screen.fill(FIRST_COLOUR)

        #draw balls
        for ball in ball_list:
            pygame.draw.circle(screen, RANDOM_COLOUR, [ball.x, ball.y], BALL_SIZE)

        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    main()