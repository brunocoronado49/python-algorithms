import random


#? Ingresar un numero x para adivinar si es el elegido de la computadora
def find_number(number):
    #* This will be the target
    target = random.randint(1, number)
    prediction = 0

    while prediction != target:
        prediction = int(input(f"Ingresa un numero entre 1 y {number}: "))

        if prediction < target:
            print(f"Este numero es menor, ingresa otro.")
        elif prediction > target:
            print("Este numero es mayor, ingresa otro")
        
    print(f"Felicidades!!! El numero es: {target}")

find_number(12)