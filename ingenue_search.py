import time
import random

def ingenue_search(target, order_list):
    for i in range(len(order_list)):
        if order_list[i] == target:
            return i
    
    return -1

if __name__=='__main__':
    size = 30000
    randoms = set()

    while len(randoms) < size:
        randoms.add(random.randint(-3 * size, 3 * size))

    my_order_list = sorted(list(randoms))

    inicio = time.time()

    for objetivo in my_order_list:
        ingenue_search(objetivo, my_order_list)

    fin = time.time()

    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")