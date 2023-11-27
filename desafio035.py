print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 035\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'DICIONARIO':^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
ford = {'Marca': 'ford', 'Modelo': 'hb20', 'Ano': 2020, 'Cor': 'cinza', 'quilometragem': 33000}
volkswagen = {'Marca': 'Volkswagen', 'Modelo': 'Jeta', 'Ano': 2023, 'Cor': 'preto', 'quilometragem': 53000}
bmw = {'Marca': 'bmw', 'Modelo': '320i', 'Ano': 2018, 'Cor': 'branco', 'quilometragem': 127000}
carros = list()
carros.append(ford)
carros.append(volkswagen)
carros.append(bmw)
for c in carros:
    print('_'*24)
    for k,v in c.items():
        print(f"{k}:", v)
print('_'*24)