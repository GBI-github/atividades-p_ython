print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 73 \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'TUPLAS' :^32}\033[0m")
print(f"{'BRASILEIRÃO':^32}")
print(f"\033[4;37m{'-' * 32}\033[0m")
print()
print("Classificação: ")
times = ("0","Botafogo", "Flamengo", "Fluminense", "Palmeiras", "Red Bull Bragantino", "Grêmio", "Atlético Paranaense", "Cuiabá Esporte Clube", "São Paulo", "Atlético Mineiro", "Cruzeiro", "Internacional", "Fortaleza", "Corinthians", "Goiás", "Bahia", "Santos", "Coritiba", "Vasco da Gama", "América FC")
for c in range(1, len(times)):
    print(f"{c}.{times[c]}")
print()
print("Os 5 maiores:")
print("1-",end="")
for c in range(1, 6):
    print(f"{times[c]}",end="")
    if c < 5:
        print(",",end=" ")

print()
print("\nOs 5 ultimos:")
print("2-", end="")
for c in range(16, 21):
    print(f"{times[c]}",end="")
    if c < 20:
        print(",",end=" ")
print()
print("\nVasco esta na posição 19º ")
print("Nomes em ordem alfabetica: ")
print(sorted(times),",")




