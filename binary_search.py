import time
import random


def ingenue_search(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

 
#* Binary search needs the number to find (target), the beginning and limit number all in a list of numbers
def binary_search(target, my_list, begining = None, limit = None):
    #* initialice the beggining and limit
    if begining is None:
        begining = 0

    if limit is None:
        limit = 0

    #* If the limit is less than beginning finish the porogramm
    if limit < begining:
        return -1
    

    #* Search the middle point 
    middle_point = (begining + limit) // 2

    #* finally the logic, make the magic
    if my_list[middle_point] == target:
        return middle_point
    elif middle_point < my_list[middle_point]:
        #* recursive function
        return binary_search(target, my_list, begining, limit -1)
    else:
        return binary_search(target, my_list, begining + 1, limit)
    
if __name__ == '__main__':
    size = 30000
    randoms = set()

    while len(randoms) < size:
        randoms.add(random.randint(-3 * size, 3 * size))

    order = sorted(list(randoms))

    first_time = time.time()
    
    for objetivo in order:
        binary_search(objetivo, order)

    last_time = time.time()

    print(f'Binary search result time: {last_time - first_time} seconds.')