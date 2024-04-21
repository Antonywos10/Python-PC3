import random

def generar_numeros():
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

def mostrar_lista(lista):
    print("Lista de números generados:")
    print(lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)

import aleatorios

# Generar la lista de números aleatorios
numeros_generados = aleatorios.generar_numeros()

# Mostrar la lista obtenida por pantalla
aleatorios.mostrar_lista(numeros_generados)

# Ordenar los valores de la lista y mostrarla por pantalla
aleatorios.ordenar_lista(numeros_generados)
