def metodo_burbuja(array):
    longitud = len(array) - 1
    
    # bucle para pasadas
    for i in range(0, longitud):
        # bucle para comparar
        for j in range(0, longitud):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
        
    return array


lista = [23, 54, 32, 12, 65, 0, 8, 76, 54, 10]

print(f"Antes de ordenar: {lista}")
metodo_burbuja(lista)
print(f"Despues de ordenar: {lista}")