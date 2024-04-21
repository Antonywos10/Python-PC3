def obtener_calificaciones():
    # Solicitar al usuario que ingrese las calificaciones separadas por comas
    calificaciones_entrada = input("Ingrese las calificaciones separadas por comas (ej. 80,90,100): ")
    
    # Intentar dividir la cadena en una lista de calificaciones y convertirlas a enteros
    try:
        # Dividir la cadena en una lista usando las comas como separador
        lista_calificaciones = calificaciones_entrada.split(',')
        
        # Convertir cada elemento de la lista a entero
        calificaciones = [int(calificacion) for calificacion in lista_calificaciones]
        
        # Retornar la lista de calificaciones
        return calificaciones
    
    except ValueError:
        # Informar al usuario sobre el error de tipeo o formato
        print("Error: Asegúrese de ingresar solo números enteros separados por comas.")
        return []

# Ejecutar la función y mostrar las calificaciones
calificaciones = obtener_calificaciones()
if calificaciones:  # Verificar si la lista no está vacía
    print("Calificaciones ingresadas correctamente:", calificaciones)

