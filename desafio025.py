print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 025\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'CIDADES' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
cidades_brasil = [
    "são paulo",
    "rio de janeiro",
    "belo horizonte",
    "salvador",
    "brasília",
    "curitiba",
    "fortaleza",
    "recife",
    "porto alegre",
    "manaus",
    "belém",
    "goiânia",
    "guarulhos",
    "campinas",
    "são luís",
    "são gonçalo",
    "maceió",
    "duque de caxias",
    "nova iguaçu",
    "são bernardo do campo",
    "teresina",
    "natal",
    "campo grande",
    "osasco",
    "santo andré",
    "joão pessoa",
    "jaboatão dos guararapes",
    "são josé dos campos",
    "contagem",
    "ribeirão preto",
    "uberlândia",
    "feira de santana",
    "sorocaba",
    "niterói",
    "cuiabá",
    "aracaju",
    "juiz de fora",
    "londrina",
    "belford roxo",
    "joinville",
    "niterói",
    "são joão de meriti",
    "ananindeua",
    "florianópolis",
    "santos",
    "ribeirão das neves",
    "vila velha",
    "serra",
    "diadema",
    "campos dos goytacazes",
    "carapicuíba"
]

print("\033[0;31mEXIT[0] \033[0m ")
cidade = ''
while cidade != '0' :
    print(f"\033[32m{'TOP 50 CIDADES' :^32}\033[0m")
    print(f"Veja se a sua esta aqui!!!")
    cidade = input("Sua cidade: ").strip().lower()
    if cidade == "0":
        print()
        print("\033[0;31mFINALIZADO \033[0m ")
    else:
        if any(c == cidade for c in cidades_brasil):
            print("Sua cidade está no top 50")
            print()
        else:
            print("Sua cidade não está nesse top 50")




