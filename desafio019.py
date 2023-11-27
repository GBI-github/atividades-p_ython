import pygame
import sys
from pygame.locals import *

pygame.init()

# Configurações da tela
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Carinha Sorrindo')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    # Desenhar a carinha
    pygame.draw.circle(screen, yellow, (width//2, height//2), 100)
    pygame.draw.circle(screen, black, (width//2 - 40, height//2 - 30), 15)
    pygame.draw.circle(screen, black, (width//2 + 40, height//2 - 30), 15)
    pygame.draw.arc(screen, black, (width//2 - 40, height//2 + 5, 100, 55), 10 , 6 , 3)
    pygame.display.update()
