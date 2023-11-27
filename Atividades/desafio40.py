def lista():
    import random
    lis = list()
    for c in range(0, 10):
        a = random.randint(0, 30)
        lis.append(a)
    return lis


lista()
print("Lista: ", lista())


def media(media_lista):
    media_lista = sum(media_lista) / len(media_lista)
    return media_lista


print("Media: ", media(lista()))
