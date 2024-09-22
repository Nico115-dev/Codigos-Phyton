def calcular_creditos():
    numero_de_materias = int(input("Ingrese el número de materias que ha cursado: "))
    total_creditos = 0
    for i in range(numero_de_materias):
        puntaje = float(input(f"Ingrese el puntaje de la materia: "))
        if puntaje >= 60:
            print(f"La materia ha sido aprobada.")
            total_creditos += 3
        else:
            print(f"La materia {i+1} no ha sido aprobada.")
    print(f"El número total de créditos obtenidos es: {total_creditos}")
calcular_creditos()
