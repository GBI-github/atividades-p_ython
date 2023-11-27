import random
print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 011\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'JOGO DA FORCA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'ADIVINHE A PALAVRA QUE EU ESTOU PENSANDO' :^32}")

palavras = [
    "cachorro", "gato", "elefante", "leão", "banana", "computador", "sol", "lua", "mesa", "cadeira",
    "carro", "bicicleta", "papel", "caneta", "livro", "chave", "porta", "janela", "telefone", "relógio",
    "camiseta", "calça", "sapato", "boné", "óculos", "colher", "garfo", "prato", "copo", "xícara",
    "martelo", "prego", "parafuso", "chave de fenda", "escada", "escova", "pente", "espelho", "espelho",
    "garrafa", "teclado", "mouse", "monitor", "tela", "carne", "arroz", "feijão", "macarrão", "pizza",
    "batata", "tomate", "cenoura", "abacaxi", "laranja", "morango", "maçã", "uva", "melancia", "abóbora",
    "viagem", "férias", "escola", "trabalho", "amor", "família", "amigo", "música", "filme", "foto",
    "praia", "montanha", "parque", "floresta", "rio", "lago", "céu", "estrela", "nuvem", "chuva",
    "amarelo", "vermelho", "azul", "verde", "rosa", "preto", "branco", "cinza", "laranja", "roxo",
    "feliz", "triste", "surpreso", "zangado", "calmo", "cansado", "ansioso", "assustado", "animado", "confuso"]

palavra = random.choice(palavras)
letras_acertadas = ["_"] * len(palavra)



def substituir_letra(palavra, letras_acertadas, letra):
    for i in range(len(palavra)):
        if letra == palavra[i] :
            letras_acertadas[i] = letra


for contador in range(0, len(palavra)):
    letra = str(input("Informe uma letra: "))
    substituir_letra(palavra, letras_acertadas, letra)
    interface = " ".join(letras_acertadas)
    print(interface)


