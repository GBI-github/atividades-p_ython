
dados1 = {"nome": "adriano", "idade": 18}
dados2 = {"nome1": "fernando", "idade1": 26}
dados3 = dict(nome2="alberto", idade2=60)

dados1["nome"] = dados2['nome1']
dados3["idade2"] = dados1["idade"]
print(dados3)

