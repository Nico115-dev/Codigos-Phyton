def calcular_costo_estacionamiento(horas):
    if horas <0:
        return "El numero de horas debe ser positivo"
    if horas <= 1:
        costo = 5
    elif horas <= 4:
        costo = 5 + (horas - 1) * 4
    else:
        costo = 5+3 * 3 + (horas - 4) * 3
    return costo
horas = float(input("Ingrese numero de horas en el estacionamiento: "))
costo_total = calcular_costo_estacionamiento (horas)
print(f"El costo de estacionamiento es: {costo_total}. ")