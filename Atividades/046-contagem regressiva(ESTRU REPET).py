import time 
import pygame
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 46\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'ESTRUTURA DE REPETIÇÃO' :^32}\033[0m")
print(f"{'CONTAGEM REGRESSIVA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
for contador in range(10, 0, -1):
    print(contador)
    time.sleep(1)

pygame.init()

pygame.mixer.music.load('manos.mp3')

pygame.mixer.music.play()

pygame.event.wait()
