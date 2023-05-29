def Ejercicio8Bisiesto():
    # Entrada
    try:
        # Asignamos a la variable el valor introducido por el usuario
        Year = int(input("Introduzca el año: "))
        # Proceso
        # Asignamos a la variable Bisiesto el resto de dividir Year entre 4
        Bisiesto = (Year % 4)
        # Si el resto es 0 asignamos a la variable Mostrar Es bisiesto
        if Bisiesto == 0:
            Mostrar = "Es bisiesto "
        # En caso contrario mostrar que no lo es
        else:
            Mostrar = "No es bisiesto "
        # Salida
        print(Mostrar)

    # Si se introduce algún valor no entero, o por algun motivo falle, mostrará Error
    except:
        print('Error ')
