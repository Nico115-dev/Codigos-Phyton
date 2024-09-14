nota = float(input("Seleccione su nota (0-100): "))
if 90 <= nota <= 100:
    calificacion = "A"
elif 80 <= nota <= 89:
    calificacion = "B"
elif 70 <= nota <= 79:
    calificacion = "C"
elif 60 <= nota <= 69:
    calificacion = "D"
elif nota <60:
    calificacion = "E"
else:
    calificacion = "Nota no valida"
print(f"la calificacion para la nota {nota} es {calificacion}. ")