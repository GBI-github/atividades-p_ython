import math
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 18\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'BLIBLIOTECA MATH' :^32}\033[0m")
print(f"{'SENO, COSSENO, TANGENTE':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
angulo = int(input("Digite o angulo que você deseja: "))
radian = math.radians(angulo)
print(f"O angulo de {angulo} tem o SENO de {math.sin(radian):.2f}\n"
      f"O angulo de {angulo} tem o COSSENO de {math.cos(radian):.2f}\n"
      f"O angulo de {angulo} tem a TANGENTE de {math.tan(radian):.2f}")