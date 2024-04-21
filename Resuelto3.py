import math

class Circulo:
    def __init__(self, radio):
        """
        Inicializador de la clase Circulo.
        
        Args:
        radio (float): El radio del círculo.
        """
        self.radio = radio
    
    def calcular_area(self):
        """
        Calcula el área del círculo utilizando la fórmula del área A = π * r^2.
        
        Returns:
        float: El área del círculo.
        """
        return math.pi * self.radio ** 2

# Crear un objeto Circulo con un radio específico
circulo = Circulo(5)

# Calcular y mostrar el área del círculo
area = circulo.calcular_area()
print(f"El área del círculo de radio {circulo.radio} es {area:.2f}")
