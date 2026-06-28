# Companion

## ¿Qué es?
Companion es un repositorio para practicar formación de código profesional. Su objetivo es evolucionar progresivamente mientras se practican conceptos como validación de datos, testing, Git y buenas prácticas.

## ¿Qué hace?
Companion por ahora permite ingresar un correo electrónico y un número de teléfono, validarlos y normalizarlos. 
## Estructura del proyecto
```text
companion/
│
├── main.py              # Punto de entrada
├── formularios.py       # Entrada de datos
├── src/
│   └── validaciones.py  # Validaciones
└── tests/
    ├── test_formularios.py
    └── test_validaciones.py
```
## Requisitos
- Python 3
## Ejecutar la aplicación
```bash
python3 main.py
```
## Ejecutar Tests
Desde repositorio "companion", ejecutar:
```bash
python3 -m tests.test_validaciones
python3 -m tests.test_formularios
```
## Próximas mejoras
- Base de datos
- Modelos
- Acciones del sistema
- Mejorar arquitectura del proyecto.
- Incorporar pytest

## Estado del proyecto

🚧 En desarrollo.

Este proyecto forma parte de un proceso de aprendizaje y evolucionará incorporando nuevas funcionalidades y mejores prácticas de desarrollo.

## Prueba github
Primera edición realizada directamente desde GitHub.
