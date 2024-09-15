import random
def adivinar_numero():
    numero_secreto = random.randint(1, 10)
    adivinado = False
    print("He generado un número entre 1 y 10. Intenta adivinarlo.")
    while not adivinado:
        try:
            intento = int(input("Ingresa tu intento: "))
            if intento < 1 or intento > 10:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue
            if intento < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_secreto}.")
                adivinado = True
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
adivinar_numero()
