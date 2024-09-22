def clasificar_triangulo(a, b, c):
    if a + b + c != 180:
        return "Los ángulos no forman un triángulo válido."
    if a == 90 or b == 90 or c == 90:
        return "Rectángulo"
    elif a > 90 or b > 90 or c > 90:
        return "Obtuso"
    else:
        return "Agudo"
try:
    a = float(input("Ingrese el primer ángulo en grados: "))
    b = float(input("Ingrese el segundo ángulo en grados: "))
    c = float(input("Ingrese el tercer ángulo en grados: "))
    tipo_triangulo = clasificar_triangulo(a, b, c)
    print(f"El triángulo es de tipo: {tipo_triangulo}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos para los ángulos.")