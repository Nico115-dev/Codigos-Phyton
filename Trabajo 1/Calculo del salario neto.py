Salario_bruto = float(input("Ingrese su salario bruto "))
Pais_De_Residencia = input("Ingrese su pais de residencia (Pais A, Pais B, Pais C): ")
if Pais_De_Residencia == "Pais A":
    porcentaje_impuesto = 0.20
elif Pais_De_Residencia == "Pais B":
    porcentaje_impuesto = 0.15
elif Pais_De_Residencia == "Pais C":
    porcentaje_impuesto = 0.10
else:
    porcentaje_impuesto = 0.25
impuesto = Salario_bruto * porcentaje_impuesto
salario_neto = Salario_bruto - impuesto
print(f"Su salario neto es {salario_neto:}")