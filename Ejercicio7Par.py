def Ejercicio7Par():
    # Entrada
    try:
        # Asignamos a numero el valor numérico entero que introduzca el usuario
        numero = int(input("Introduzca un número entero: "))

        # Proceso
        # En resultado añadimos el resto de numero al dividirlo entre 2
        resultado = numero % 2

        # Si el resultado es 0 es par y si es 1 impar, asignaremos el resultado en mostrar
        if resultado == 0:
            mostrar = "Es par "
        elif resultado == 1:
            mostrar = "Es impar "
        else:
            mostrar = "Resultado inesperado "

        # Salida
        # Mostramos el valor de la variable mostrar por la pantalla
        print(mostrar)

        # Si se introduce algún valor no entero, o por algun motivo falle, mostrará Error
    except:
        print('Error ')
