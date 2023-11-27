print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 104\033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'FUNÇÃO DEF' :^32}\033[0m")
print()
print(f"\033[32m{'INTERATIVE HELP':^32}\033[0m")
print()


def interative(duvida):
    while True:
        duvida = str(input(duvida))
        print()
        print(f"\033[37m{'-' * 32}\033[0m")
        print("\033[34m")
        help(duvida)
        print("\033[0m")
        print(f"\033[37m{'-' * 32}\033[0m")
        cont = str(input("\033[31mEnd\033[0m/\033[32mContinue: \033[0m")).lower().strip()
        if cont == "end":
            break
        duvida = "\033[32minforme a função que tem duvida:\033[0m "


interative("\033[32minforme a função que tem duvida:\033[0m  ")
print()
print("\033[31mFIM\033[0m\033[34m Interative help\033[0m")