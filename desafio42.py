def lista():
    import random
    lis = list()
    for c in range(0, 10):
        a = random.randint(0, 30)
        lis.append(a)
    return lis


def maior_numero(num):
    print(num)
    maior = max(num)
    print(maior)


maior_numero(lista())