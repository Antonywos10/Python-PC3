class Alumno:
    def __init__(self, nombre, numero_registro):
        """
        Inicializa el objeto Alumno con nombre y número de registro.
        
        Args:
        nombre (str): Nombre del alumno.
        numero_registro (int): Número de registro del alumno.
        """
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
    
    def display(self):
        """
        Muestra toda la información del alumno, incluyendo nombre, número de registro,
        edad (si está asignada) y notas (si están asignadas).
        """
        info = f"Nombre: {self.nombre}\nNúmero de Registro: {self.numero_registro}"
        if self.edad is not None:
            info += f"\nEdad: {self.edad}"
        if self.notas:
            info += f"\nNotas: {', '.join(map(str, self.notas))}"
        print(info)
    
    def setAge(self, edad):
        """
        Asigna la edad al alumno.
        
        Args:
        edad (int): Edad del alumno.
        """
        self.edad = edad
    
    def setNota(self, notas):
        """
        Asigna las notas al alumno.
        
        Args:
        notas (list): Lista de notas del alumno.
        """
        self.notas = notas

# Ejemplo de uso de la clase Alumno
alumno = Alumno("Juan Pérez", 12345)
alumno.setAge(20)
alumno.setNota([85, 92, 78, 90])
alumno.display()

