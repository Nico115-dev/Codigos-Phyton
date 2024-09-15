Distancia = float(input("Ingrese la distancia a recorrer (en km): "))
Velocidad = float(input("Ingrese velocidad promedio (en km/h): "))
tiempo_horas = Distancia / Velocidad
horas = int(tiempo_horas)
minutos = int((tiempo_horas - horas) * 60)
print(f"tiempo de viaje: {horas} horas y {minutos} minutos")
if Velocidad > 120:
    print("Advertencia: !Baja la velocidad!. ")