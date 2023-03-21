def ordenacion_shell(array):
    longitud = len(array)
    intervalo = longitud // 2
    
    while intervalo > 0:
        for i in range(intervalo, longitud):
            insert_value = array[i]
            insert_index = i
            
            while insert_index >= intervalo and array[insert_index - intervalo] > insert_value:
                array[insert_index] = array[insert_index - intervalo]
                insert_index -= intervalo
                
            array[insert_index] = insert_value
            
        # actualizamos el intervalo
        intervalo //= 2
    return array

scores = [23, 54, 32, 12, 65, 0, 8, 76, 54, 10]

print(f"Antes de ordenar: {scores}")
result = ordenacion_shell(scores)
print(f"Despues de ordenar: {result}")