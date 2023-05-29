def Ejercicio6Fahrenheit():

    # Entrada
    try:
        # Se asigna a Celcius el valor que introduzca el usuario
        Celcius = float(input("Introduzca los grados Celcius: "))
        # Proceso
        # Se asigna a Fahrenheit el valor de la operación para saber cuantos Fahrenheit tiene los Celcius
        Fahrenheit = ((Celcius*1.8)+32)
        # Salida
        # Mostramos el resultado por la pantalla
        print("Son: {n:8.2f} grados Fahrenheit".format(n=Fahrenheit))
    # En caso de no introducir un número válido mostrará error
    except:
        print("Error, no introdujo un valor válido de grados Celcius ")
