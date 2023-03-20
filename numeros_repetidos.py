from collections import Counter


def numeros_repetidos(numeros):
    return dict(Counter(numeros))

lista_numeros = [1, 2, 3, 3, 4, 4, 5, 6, 6]
result = numeros_repetidos(lista_numeros)

print(result)