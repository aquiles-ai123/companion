from formularios import pedir_correo, pedir_telefono

def main():
    correo = pedir_correo()
    telefono = pedir_telefono()
    print("Tu Correo es: ",correo)
    print("Tu teléfono es: ", telefono)

main()
