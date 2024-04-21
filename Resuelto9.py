
def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero"
        else:
            resultado = a / b
            return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

import operaciones

# Ejemplos de uso de las funciones del módulo operaciones
print("Suma:", operaciones.suma(5, 3))
print("Resta:", operaciones.resta(8, 2))
print("Producto:", operaciones.producto(4, 6))
print("División:", operaciones.division(10, 2))


