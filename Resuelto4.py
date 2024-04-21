class Rectangulo:
    def __init__(self, largo, ancho):
        """
        Inicializador de la clase Rectangulo.
        
        Args:
        largo (float): El largo del rectángulo.
        ancho (float): El ancho del rectángulo.
        """
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        """
        Calcula el área del rectángulo utilizando la fórmula del área A = largo * ancho.
        
        Returns:
        float: El área del rectángulo.
        """
        return self.largo * self.ancho

# Ejemplo de uso de la clase Rectangulo
rectangulo = Rectangulo(10, 5)

# Calcular y mostrar el área del rectángulo
area = rectangulo.calcular_area()
print(f"El área del rectángulo de largo {rectangulo.largo} y ancho {rectangulo.ancho} es {area}")
