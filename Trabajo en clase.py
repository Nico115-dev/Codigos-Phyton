import os

def InsertData(scr: list):
    contact = input('Ingrese el nombre del contacto: ').strip()
    if contact:
        scr.append(contact)
    else:
        print("El nombre del contacto no puede estar vacío.")

def VerData(scr: list):
    if not scr:
        print("No hay contactos registrados.")
    else:
        for data in scr:
            print(data)

def EliminarData(scr: list):
    contact = input('Ingrese el nombre del contacto a eliminar: ').strip()
    if contact in scr:
        scr.remove(contact)
        print(f'Contacto "{contact}" eliminado con éxito.')
    else:
        print(f'El contacto "{contact}" no está registrado.')

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(titulo)
    print(menu)

if __name__ == "__main__":
    agendate1 = []
    isActive = True
    menu = '1. Registrar Contacto\n2. Listar Contactos\n3. Eliminar Contacto\n4. Salir'
    titulo = """
        *

REGISTRO DE CONTACTOS J2 **"""

    while isActive:
        display_menu()
        try:
            op = int(input(':) '))
            match op:
                case 1:
                    isAddContact = True
                    while isAddContact:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        InsertData(agendate1)
                        isAddContact = input('¿Desea ingresar otro contacto? (S/N): ').strip().lower() == 's'
                case 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    VerData(agendate1)
                    input("Presione Enter para continuar...")  # Pause to view contacts
                case 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    EliminarData(agendate1)
                    input("Presione Enter para continuar...")  # Pause after deletion
                case 4:
                    isActive = input('¿Desea abandonar el programa? (S/N): ').strip().lower() == 'n'
                case _:
                    print("Opción no válida, por favor intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")