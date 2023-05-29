def Ejercicio11Factorial():
    # Entrada
    try:
        numero = int(
            input("Introduce un número entero del que quieras calcular el factorial: "))
        contador = 0
        factorial = 1

    # Proceso
        # Si el numero introducido es negativo el bucle no llegará a terminar nunca
        # con un if calculamos que no sea menor a 0, si lo es indicamos el error por la pantalla
        if numero < contador:
            print("No podemos calcular el valor factorial de un número negativo")
        # Si el número no es negativo continuamos
        else:
            # Creamos un bucle que se repetirá mientras contador no sea igual a numero
            while contador != numero:
                contador = contador+1
                factorial = factorial*contador
        # Salida
            # Mostramos por la pantalla el valor factorial del numero introducido por el usuario
            print("El facorial de ", numero, " es ", factorial)
    # Antes un valor no entero o otro error inesperado mostramos Error
    except:
        print("Error")
