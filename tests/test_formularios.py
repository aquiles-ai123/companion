from formularios import ingresar_correo,ingresar_telefono

casos_telefono = [
     ("12345678", "12345678"), ("1234567890", "1234567890"), ("123456789012345", "123456789012345"),
     ("1234567", "Teléfono inválido"), ("1234567890123456", "Teléfono inválido"), ("12345abc", "Teléfono inválido"),
     ("", "Teléfono inválido"), ("1234 5678","12345678"), ("1234-5678", "12345678"), ("+56912345678", "56912345678"),
]

casos_correo = [
    ("ana@gmail.com", "ana@gmail.com"),
    ("a@b.com", "a@b.com"),
    ("ana@gmailcom", "Correo inválido"),
    ("anagmail.com", "Correo inválido"),
    ("@gmail.com", "Correo inválido"),
    ("ana@gmail.", "Correo inválido"),
    ("", "Correo inválido"),
    ("@", "Correo inválido"),
    ("ana@@gmail.com", "Correo inválido"),
    ("ana@gmail..com", "Correo inválido"),
]


def test_formularios():
    for telefono, esperado in casos_telefono:
        assert ingresar_telefono(telefono) == esperado
    for correo,esperado in casos_correo:
        assert ingresar_correo(correo) == esperado 
test_formularios()
print("Todos los tests de formularios.py pasaron")
