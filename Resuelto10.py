import math

class Circulo:
    def calcular_area(self, radio):
        return math.pi * radio ** 2

class Rectangulo:
    def calcular_area(self, base, altura):
        return base * altura

class Cuadrado:
    def calcular_area(self, lado):
        return lado ** 2

def mostrar_menu():
    print("Menu:")
    print("1. Calcular área de un círculo")
    print("2. Calcular área de un rectángulo")
    print("3. Calcular área de un cuadrado")
    print("4. Salir")

def main():
    circulo = Circulo()
    rectangulo = Rectangulo()
    cuadrado = Cuadrado()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            area = circulo.calcular_area(radio)
            print("El área del círculo es:", area)
        elif opcion == '2':
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = rectangulo.calcular_area(base, altura)
            print("El área del rectángulo es:", area)
        elif opcion == '3':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = cuadrado.calcular_area(lado)
            print("El área del cuadrado es:", area)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
