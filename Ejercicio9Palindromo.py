def Ejercicio9Palindromo():
    # Entrada
    # Asignamos a cadena el valor introducido por el usuario
    cadena = input(
        "Introduzca una cadena para averiguar si es un palíndromo o no: ")
    # Asignamos a cadenaMinuscula La cadena modificada para que todo sea en minúscula
    cadenaMinuscula = cadena.lower()
    # Proceso
    # Comparamos el valor de cadenaMinuscula con su reversa, si son iguales, asignamos a la variable resultado "es palíndromo"
    if str(cadenaMinuscula) == "".join(reversed(cadenaMinuscula)):
        resultado = "La cadena es un palíndromo "
    # Si no es igual asignamos a resultado "no es palíndromo"
    else:
        resultado = "La cadena no es un palíndromo "

    # Salida
    # Mostramos resultado por la pantalla
    print(resultado)
