def imprimir_numeros_pares(inicio, fin):
    if inicio > fin:
        print("El valor de inicio debe ser menor o igual al valor de fin.")
        return
    if inicio % 2 != 0:
        inicio += 1
    for numero in range(inicio, fin + 1, 2):
        print(numero)
try:
    inicio = int(input("Ingrese el valor de inicio: "))
    fin = int(input("Ingrese el valor de fin: "))
    imprimir_numeros_pares(inicio, fin)
except ValueError:
    print("Por favor, ingrese números enteros válidos.")