print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 009\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'VERIFICADOR DE E-MAIL' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'Criar e-mail' :^32}")
print("*@gmail.com*")
email = input("Digite email: ").strip()
email_validar = email.find("@gmail.com")
if email_validar == -1:
    print("email invalido")
    print("Falta *@gmail.com* ")
else:
    print("email valido ")
