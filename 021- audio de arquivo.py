import pygame
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 21\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'BLIBLIOTECA PYGAME' :^32}\033[0m")
print(f"{'MUSICA':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
pygame.init()
pygame.mixer.music.load('ex01,mp3')
pygame.mixer.music.play()
pygame.event.wait()