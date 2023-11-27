print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 031\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'TUPLA FRUTA- REVERSED' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
frutas = ("Abacaxi", "Banana",
          "Maçã",
          "Laranja",
          "Pera",
          "Uva",
          "Morango",
          "Manga",
          "Limão",
          "Cereja",
          "Kiwi",
          "Melancia",
          "Melão",
          "Pêssego",
          "Framboesa",
          "Amora",
          "Goiaba",
          "Caju",
          "Ameixa",
          "Coco",
          "Jabuticaba",
          "Caqui",
          "Figo",
          "Tangerina",
          "Maracujá",
          "Pitanga",
          "Abacate",
          "Lichia",
          "Romã",
          "Carambola",
          "Physalis",
          "Pera",
          "Guaraná",
          "Açaí",
          "Cajuí",
          "Graviola",
          "Jaca",
          "Pinha",
          "Umbu",
          "Seriguela",
          "Jambo",
          "Cupuaçu",
          "Burahem",
          "Araticum",
          "Tamarindo",
          "Cambuci",
          "Biribá",
          "Cajá",
          "Cajamanga")
c2 = ''
c3 = 0
frutas_reversas = []
for c in range(0, len(frutas)):
    for c1 in reversed(frutas[c]):
        c2 += c1
    frutas_reversas.append(c2)
    c2 = ''
    c3 += 1
for c in range(0, len(frutas)):
    print(f"{frutas[c]:.<20}{frutas_reversas[c].title()}")
