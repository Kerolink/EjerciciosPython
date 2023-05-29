# Entrada
def Ejercicio15NegativoPositivoCero():
    try:
        # Asignamos a numero el valor que el usuario introduzca
        numero = float(input("Introduzca un número: "))
        # Proceso
        # Si el numero es mayor a 0 asignamos a resultado es positivo
        if numero > 0:
            resultado = "Es positivo "
        # Si el numero es menor a 0 asignamos a resultado es negativo
        elif numero < 0:
            resultado = "Es negativo "
        # Si el numero es 0 asignamos a resultado es cero
        elif numero == 0:
            resultado = "Es cero "
        # Si no cumple nada de lo anterior asignamos a resultado ocurrio un error
        else:
            resultado = "Ocurrió un error "
            # Salida
        # Mostramos por pantalla resultado
        print(resultado)
    # El programa podría fallar al intentar introducir letras, por ejemplo
    except:
        print("Error")
