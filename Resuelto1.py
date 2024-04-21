def leer_fraccion():
    while True:
        entrada = input("Ingrese la fracción (X/Y): ")
        try:
            # Intentar dividir la entrada en dos partes: X e Y
            x, y = map(int, entrada.split('/'))
            # Validar que X sea menor o igual que Y y Y no sea 0
            if x > y or y == 0:
                raise ValueError("X debe ser menor o igual a Y y Y debe ser diferente de 0.")
            
            # Calcular el porcentaje
            porcentaje = (x / y) * 100

            # Verificar los límites del porcentaje para determinar la salida
            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{round(porcentaje)}%"

        except ZeroDivisionError:
            print("Error: No se puede dividir por cero. Intente nuevamente.")
        except ValueError:
            print("Error: Asegúrese de que ambos valores sean enteros y X no sea mayor que Y. Intente nuevamente.")

# Ejecutar el programa
resultado = leer_fraccion()
print("Resultado:", resultado)

