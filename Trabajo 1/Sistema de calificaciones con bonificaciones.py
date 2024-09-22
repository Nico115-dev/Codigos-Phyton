Calificacion = float(input("Ingrese su calificacion: "))
tareas_adicionales = input("El estudiante realizó tareas adicionales? (Si/No)").strip()
if tareas_adicionales == "sí" or tareas_adicionales == "si":
    Calificacion += Calificacion * 0.5
    if Calificacion > 100:
        Calificacion = 100
print(f"La calificacion final es {Calificacion}")
