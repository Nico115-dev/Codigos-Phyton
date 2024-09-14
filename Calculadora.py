print("Selecciona una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = input("Introduce el número de la operación (1/2/3/4): ")
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
match opcion:
    case "1":
        resultado = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es {resultado}.")
    case "2":
        resultado = numero1 - numero2
        print(f"La resta de {numero1} y {numero2} es {resultado}.")
    case "3":
        resultado = numero1 * numero2
        print(f"La multiplicación de {numero1} y {numero2} es {resultado}.")
    case "4":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"La división de {numero1} entre {numero2} es {resultado}.")
        else:
            print("Error: No se puede dividir entre cero.")
    case _:
        print("Opción inválida. Por favor, elige un número entre 1 y 4.")