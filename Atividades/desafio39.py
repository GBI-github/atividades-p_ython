def soma(a=0, b=0, ad=0):
    import random
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    ad = a + b
    print(f"{a} + {b} = ", end="")
    return ad


e = r = l = 0
print(soma(e, r, l))
