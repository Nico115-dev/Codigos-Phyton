def adivinar_letra():
    letra_secreta = 'A'
    adivinanza = input("Adivina la letra secreta: ").upper()
    if adivinanza == letra_secreta:
        print("¡Correcto! Has adivinado la letra secreta.")
    else:
        print("Incorrecto. La letra secreta era:", letra_secreta)
adivinar_letra()