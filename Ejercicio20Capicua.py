def Ejercicio20Capicua():
    # Entrada
    # Asignamos a cadena el valor introducido por el usuario
    cadena = input(
        "Introduzca un número para averiguar si es un capicúa o no: ")
    # Asignamos a cadenaMinuscula La cadena modificada para que todo sea en minúscula
    cadenaMinuscula = cadena.lower()
    try:
        int(cadena)
        # Proceso
        # Comparamos el valor de cadenaMinuscula con su reversa, si son iguales, asignamos a la variable resultado "es capicúa"
        if str(cadenaMinuscula) == "".join(reversed(cadenaMinuscula)):
            resultado = (" es capicúa ")
        # Si no es igual asignamos a resultado "no es capicúa"
        else:
            resultado = (' no es capicúa ')

        # Salida
        # Mostramos reultado por la pantalla
        print("El número ", cadena, resultado)
    except:
        print("Ha habido un error, asegúrese de que introduce un número entero ")
