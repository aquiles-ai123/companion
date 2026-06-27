from src.validaciones import validar_correo,validar_telefono

casos_telefono = [
     ("12345678", True), ("1234567890", True), ("123456789012345", True),
     ("1234567", False), ("1234567890123456", False), ("12345abc", False),
     ("", False), ("1234 5678", False), ("1234-5678", False), ("+56912345678", False),
]

casos_correo = [
    ("ana@gmail.com", True),
    ("a@b.com", True),
    ("ana@gmailcom", False),
    ("anagmail.com", False),
    ("@gmail.com", False),
    ("ana@gmail.", False),
    ("", False),
    ("@", False),
    ("ana@@gmail.com", False),
    ("ana@gmail..com", False),
]


def test_validar_correo():
    for correo, esperado in casos_correo:
        assert validar_correo(correo) == esperado
def test_validar_telefono():
    for telefono, esperado in casos_telefono:
        assert validar_telefono(telefono) == esperado
test_validar_correo()
test_validar_telefono()
print("Todos los tests de validaciones.py pasaron")




