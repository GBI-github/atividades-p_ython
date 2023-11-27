print(f"\033[4;37m{'-' * 10}\033[0;31m DESAFIO 008\033[0m \033[4;37m{'-' * 10}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"\033[32m{'VERIFICADOR DE SENHA' :^32}\033[0m")
print(f"\033[4;37m{'-' * 32}\033[0m")
print(f"{'Criar Senha' :^32}")
print("Pelo menos 8 caracteres de comprimento.\n"
      "Contém pelo menos uma letra maiúscula e uma minúscula.\n"
      "Contém pelo menos um número."
      'Contém pelo menos um simbolo ("." "_" "#" "," "@")')
print(" ")
senha = input("Digite sua senha: ")
senhavalida = "12345678"
senhainvalida = "123456789101"
caractere_verificar = [".", "_", "#", ",", "@"]
letra = senha
caractere02 = any(letra.isupper() for letra in senha)
caractere1 = any(letra.islower() for letra in senha)
numero = any(n.isnumeric() for n in senha)
simbulo_buscar = any(caractere in senha for caractere in caractere_verificar)

if len(senhainvalida) >= len(senha) >= len(senhavalida) and caractere02 and caractere1 and numero and simbulo_buscar:
    print("Senha valida")
else:
    print("Senha invalida")

