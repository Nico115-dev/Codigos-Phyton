def contar_vocales(cadena):
    vocales = 'aeiou'
    conteo = 0
    for caracter in cadena.lower():
        if caracter in vocales:
            conteo += 1
    return conteo
cadena_usuario = input("Ingrese una cadena de texto: ")
numero_vocales = contar_vocales(cadena_usuario)
print(f"La cadena contiene {numero_vocales} vocales.")