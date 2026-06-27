def validar_telefono(telefono):
    return telefono.isdigit() and 8 <= len(telefono) <= 15
def validar_correo(correo):
    if correo.startswith("@"): 
       return False
    if correo.endswith("."):
       return False
    if "@" not in correo or "." not in correo:
       return False
    if "@@" in correo or ".." in correo:
       return False
    return True



