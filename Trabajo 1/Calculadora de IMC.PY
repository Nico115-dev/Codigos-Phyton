def calcular_imc(peso, altura):
    return peso / (altura ** 2)
def clasificar_imc(imc):
    match imc:
        case _ if imc < 18.5:
            return "bajo peso"
        case _ if 18.5 <= imc < 25:
            return "peso normal"
        case _ if 25 <= imc < 30:
            return "sobrepeso"
        case _ if imc >= 30:
            return "obesidad"
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
categoria = clasificar_imc(imc)
print(f"Tu IMC es {imc:.2f} y se clasifica como {categoria}.")
