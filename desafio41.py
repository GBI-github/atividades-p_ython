import random


def a(val):
    if val % 2 == 0:
        return True

    else:
        return False


num = random.randint(1,100)
print(a(num))
