def calcular_suma_numeros_enteros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
try:
    n = int(input("Ingrese un número entero positivo: "))
    if n <= 0:
        print("El número debe ser positivo.")
    else:
        suma_total = calcular_suma_numeros_enteros(n)
        print(f"La suma de los primeros {n} números enteros es: {suma_total}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")