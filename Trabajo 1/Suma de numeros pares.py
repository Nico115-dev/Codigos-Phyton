def sumar_numeros_pares():
    suma = 0
    while True:
        try:
            numero = int(input("Ingrese un número entero (o un número impar para detener): "))
            if numero % 2 != 0:
                print("Número impar ingresado. Terminando el programa.")
                break
            if numero % 2 == 0:
                suma += numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    print(f"La suma de los números pares ingresados es: {suma}")
sumar_numeros_pares()