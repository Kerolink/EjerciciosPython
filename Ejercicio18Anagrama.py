def Ejercicio18Anagrama():
    # Entrada
    # Asignamos a String1 y 2 las cadenas que introduzca el usuario
    String1 = input("Introduzca la primera cadena: ")
    String2 = input("Introduzca la segunda cadena: ")
    # Proceso
    # Convertimos todos los caracteres a minusculas de String1 y 2 Y lo asignamos a String1Minuscula y 2 simultáneamente
    String1Minuscula = String1.lower()
    String2Minuscula = String2.lower()

    # sorted lo ordena todo en orden, si ambas cadenas son iguales asignamos a resultado "Son anagramas"
    if (sorted(String1Minuscula) == sorted(String2Minuscula)):
        resultado = "Son anagramas "
    # De lo contrario asignamos a resultado "No son anagramas"
    else:
        resultado = "No son anagramas "
    # Salida
    # Mostramos por la pantalla resultado
    print(resultado)
