from babel.numbers import format_currency

# Seu número
numero = 50

# Formate o número como moeda (use a moeda que desejar, por exemplo, "USD" para dólares)
moeda_formatada = format_currency(numero, 'BRL', locale='pt_BR')

print(moeda_formatada)




