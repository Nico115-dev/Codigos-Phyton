numero_1 = float(input("Ingrese un numero: "))
numero_2 = float(input("Ingrese un numero: "))
numero_3 = float(input("Ingrese un numero: "))
mayor = numero_1
if numero_2 > mayor:
    mayor = numero_2
if numero_3 > mayor:
    mayor = numero_3
print("El numero mayor es:", mayor)
