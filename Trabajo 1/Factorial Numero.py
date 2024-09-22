def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
try:
    n = int(input("Ingrese un número entero positivo: "))
    if n < 0:
        print("El número debe ser positivo.")
    else:
        resultado_factorial = calcular_factorial(n)
        print(f"El factorial de {n} es: {resultado_factorial}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")