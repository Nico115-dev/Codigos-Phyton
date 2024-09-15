def convertir_calificacion():
    while True:
        try:
            calificacion = float(input("Ingrese una calificación numérica (0-100): "))
            if calificacion < 0 or calificacion > 100:
                print("Por favor, ingrese un número entre 0 y 100.")
                continue
            match calificacion:
                case _ if 90 <= calificacion <= 100:
                    letra = 'A'
                case _ if 80 <= calificacion <= 89:
                    letra = 'B'
                case _ if 70 <= calificacion <= 79:
                    letra = 'C'
                case _ if 60 <= calificacion <= 69:
                    letra = 'D'
                case _:
                    letra = 'F'
            print(f"La calificación {calificacion} corresponde a una letra: {letra}")
            break  
        except ValueError:
            print("Por favor, ingrese un número válido.")
convertir_calificacion()