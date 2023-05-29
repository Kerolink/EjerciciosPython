def Ejercicio4Circulo():

    # Entrada
    try:
        Radio = float(input("Introduzca el radio del círculo: "))
        PI = 3.14

        # Proceso
        # El radio no puede ser negativo, lo comprobaremos con el siguiente if
        if Radio <= 0:
            print("Invalid Data ")
        # Una vez los datos estan correctos debería realizar las operaciones de cálculo y asignarlas a las variables Area y Perimetro
        else:
            Area = PI*Radio**2
            Perimetro = PI*(2*Radio)
        # Salida
        # Mostramos las variables Area y Perimetro por la pantalla
            print("El área del círculo es: ", Area)
            print("El perímetro del círculo es: ", Perimetro)

    # El programa podría fallar al intentar introducir letras, por ejemplo
    except:
        print("Error")
