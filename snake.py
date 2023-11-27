import pygame
import random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    return (x //10 * 10, y // 10 * 10 )

def collision(c1, c2):
    return c1[0] == c2[0] and c1[1] == c2[1]

def show_game_over_screen(screen):
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    play_again_text = font.render("Pressione ESPAÇO pra continuar", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))
    screen.blit(play_again_text, (120, 300))
    pygame.display.update()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
SPACE = 10

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.Clock()

game_over = False

while not game_over:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP

            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN

            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT

            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    if snake[0][0] < 0 or snake[0][0] >= 600 or snake[0][1] < 0 or snake[0][1] >= 600:
        game_over = True

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

show_game_over_screen(screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == SPACE:
                game_over = False
                snake = [(200, 200), (210, 200), (220, 200)]
                my_direction = LEFT
                apple_pos = on_grid_random()
                break

    if not game_over:
        show_game_over_screen(screen)
