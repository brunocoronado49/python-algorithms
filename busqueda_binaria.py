import random
import time


def busqueda_binaria(objetivo, lista, inicio = None, limite = None):
    if inicio is None:
        inicio = 0
    
    if limite is None:
        limite = 0
    
    if limite < inicio:
        return -1
    
    punto_medio = (inicio + limite ) // 2
    
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif punto_medio < lista[punto_medio]:
        return busqueda_binaria(objetivo, lista, inicio, limite - 1)
    else:
        return busqueda_binaria(objetivo, lista, inicio + 1, limite)

if __name__=='__main__':
    size = 30000
    randoms = set()
    
    while len(randoms) < size:
        randoms.add(random.randint(-3 * size, 3 * size))
        
    lista_ordenada = sorted(list(randoms))
    
    tiempo_inicio = time.time()
    
    for mi_objetivo in lista_ordenada:
        busqueda_binaria(mi_objetivo, lista_ordenada)
    
    timepo_final = time.time()
    
    print(f"El tiempo tardado es: {timepo_final - tiempo_inicio} segundos.")