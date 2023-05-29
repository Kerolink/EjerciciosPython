def Ejercicio13Cubo():
    # Entrada
    try:
        # Asignamos a la variable lado el número introducido por el usuario
        lado = float(input("Introduzca el lado del cubo: "))

        # Proceso
        # Calculamos y asignamos los valores de las siguientes formulas a Area y Volumen
        # Area <- 6 x lado^2
        Area = 6*lado**2
        # Volumen <-lado^3
        Volumen = lado**3

        # Salida
        # Mostramos por la pantalla los resultados de Area y Volumen
        print("El área del cubo es: ", Area)
        print("El volumen del cubo es: ", Volumen)
    # El programa podría fallar al intentar introducir letras, por ejemplo
    except:
        print("Error")
