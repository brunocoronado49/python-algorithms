def insert_sort(array):
    longitud = len(array)
    
    for i in range(1, longitud):
        insert_value = array[i] # toma el sig valor a ser insertado
        insert_index = i # indice donde se va a insetrar el valor
        
        while insert_index > 0 and array[insert_index - 1] > insert_value:
            array[insert_index] = array[insert_index - 1]
            insert_index -= 1
            
        # insertamos el valor en su indice correspondiente
        array[insert_index] = insert_value
    return array

scores = [23, 54, 32, 12, 65, 0, 8, 76, 54, 10]

print(f"Antes de ordenar: {scores}")
result = insert_sort(scores)
print(f"Despues de ordenar: {result}")