def encontrar_linha_produto(arquivo, produto):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
        for i, linha in enumerate(linhas, 1):
            if produto in linha:
                return i  # Retorna o número da linha onde o produto foi encontrado
    return None  # Retorna None se o produto não for encontrado no arquivo

