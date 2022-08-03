import pygame
from random import randint

from utils import *

pygame.init()

# Loading assets:
jim = jim_the_jelly(1)
LEFT = jim.left
RIGHT = jim.right

COIN = pygame.image.load("imgs/coin.png")

BG = pygame.image.load("imgs/bg.png")
BG_OTHER = pygame.image.load("imgs/bg_other.png")

# Define width & height for the app:
WIDTH, HEIGHT = BG.get_width(), BG.get_height()
SIZE = (WIDTH, HEIGHT)

# Initiate the window:
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Jim The Jellyfish!")

def draw(imgs, coin_count:int=0):
    for img in imgs:
        WIN.blit(img[0], img[1])

    font = pygame.font.Font('JetBrainsMono-Regular.ttf', 20)
    text = font.render(f"Coins: {coin_count}", True, (255, 255, 255))
    textRect = text.get_rect()
    WIN.blit(text, (10, 10))

    pygame.display.update()

def rand_coords(padding:int=50):
    x = randint(padding, WIDTH - padding)
    y = randint(padding, WIDTH - padding)
    return [x, y]

def main():
    FPS = 60
    run = True
    clock = pygame.time.Clock()
    print("[STARTING]\tThe game has been initiated at %d FPS" % FPS)
    images = [[BG, [0, 0]], [COIN, rand_coords()], [RIGHT, [100, 100]]]
    bg_time_max = 15
    bg_time_left = bg_time_max
    coin_count = 0
    while run:
        clock.tick(FPS)
        draw(images, coin_count)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("[EXITING]\tUser exited the game")
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] | keys[pygame.K_LEFT]:
            images[2][1][0] -= 10
            images[2][0] = LEFT
        if keys[pygame.K_d] | keys[pygame.K_RIGHT] :
            images[2][1][0] += 10
            images[2][0] = RIGHT
        if keys[pygame.K_w] | keys[pygame.K_UP]:
            images[2][1][1] -= 10
        if keys[pygame.K_s] | keys[pygame.K_DOWN] :
            images[2][1][1] += 10

        if keys[pygame.K_RETURN]:
            images[2][1] = [(WIDTH - images[2][0].get_width())//2, (HEIGHT - images[2][0].get_height())//2]

        if keys[pygame.K_ESCAPE]:
            print("[EXITING]\tUser used ESC to leave the program")
            run = False

        # Check for warping:
        if images[2][1][0] < 0 - images[2][0].get_width():
            images[2][1][0] = WIDTH + images[2][0].get_width()

        if images[2][1][0] > WIDTH + images[2][0].get_width():
            images[2][1][0] = 0 - images[2][0].get_width()

        if images[2][1][1] < 0 - images[2][0].get_height():
            images[2][1][1] = HEIGHT + images[2][0].get_height()

        if images[2][1][1] > HEIGHT + images[2][0].get_height():
            images[2][1][1] = 0 - images[2][0].get_height()

        # Check to see if background should change:
        if bg_time_left == 0 and images[0][0] == BG:
            images[0][0] = BG_OTHER
            bg_time_left = bg_time_max
        elif bg_time_left == 0 and images[0][0] == BG_OTHER:
            images[0][0] = BG
            bg_time_left = bg_time_max

        bg_time_left -= 1

        # Is the user touching the coin?
        if (images[2][1][0] < images[1][1][0] < images[2][1][0] + images[2][0].get_width()) and (images[2][1][1] < images[1][1][1] < images[2][1][1] + images[2][0].get_height()):
            images[1][1] = rand_coords()
            coin_count += 1

    pygame.quit()

if __name__ == "__main__":
    try:
        main();
    except KeyboardInterrupt:
        print("\r[EXITING]\tKeyboard Interrupt recieved, exiting...")
        pygame.quit()
