from src.validaciones import validar_telefono, validar_correo




def ingresar_correo(correo):
    if validar_correo(correo):
       return correo
    return "Correo inválido" 
def ingresar_telefono(telefono):
    telefono = telefono.replace(" ", "")
    telefono = telefono.replace("-", "")
    telefono = telefono.strip("+")
    if validar_telefono(telefono):
       return telefono
    else:
         return "Teléfono inválido"
def pedir_telefono():
    while True:
          telefono = input("¿Cuál es tu teléfono? ")
          telefono = ingresar_telefono(telefono)
          if telefono != "Teléfono inválido":
             print("Elegiste: ", telefono)
             return telefono
def pedir_correo():
    while True:
          correo = input("¿Cuál es tu correo? ")
          correo = ingresar_correo(correo)
          if correo != "Correo inválido":
             print("Elegiste: ",correo)
             return correo
