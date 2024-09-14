nota = float(input("Introduce la nota numérica (0.0 - 60): "))
if 0.0 <= nota <= 60:
    if nota >= 60:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("La nota ingresada no es válida. Debe estar entre 0.0 y 10.0.")
