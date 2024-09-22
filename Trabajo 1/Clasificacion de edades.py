edad = int(input("Ingrese su edad: "))
if 0 <= edad <= 12:
    categoria = "niño"
elif 13 <= edad <= 17:
    categoria = "Adolescente"
elif 18 <= edad <= 64:
    categoria = "Adulto"
elif edad >= 65:
    categoria = "Anciano"
else:
    categoria = "Edad no valida"
print(f"Tu categoria segun tu edad es: {categoria}")
    