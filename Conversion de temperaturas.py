def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def convertir_fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
opcion = input("¿Deseas convertir de Celsius a Fahrenheit (C) o de Fahrenheit a Celsius (F)? ").strip().upper()
temperatura = float(input("Ingresa la temperatura a convertir: "))
match opcion:
    case "C":
        resultado = convertir_celsius_a_fahrenheit(temperatura)
        print(f"{temperatura} grados Celsius es igual a {resultado:.2f} grados Fahrenheit.")
    case "F":
        resultado = convertir_fahrenheit_a_celsius(temperatura)
        print(f"{temperatura} grados Fahrenheit es igual a {resultado:.2f} grados Celsius.")
    case _:
        print("Opción no válida. Por favor, elige 'C' para Celsius a Fahrenheit o 'F' para Fahrenheit a Celsius.")
