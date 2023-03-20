def remove_from_list(numeros, index):
    lista = numeros.copy()
    lista.pop(index)
    return lista

mis_numeros = [1, 2, 3, 4, 5, 6, 7]
result = remove_from_list(mis_numeros, 2)

print(f"Lista original: {mis_numeros}")
print(f"Lista modificada: {result}")