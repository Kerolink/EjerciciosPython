def Ejercicio12Primo():
    # Entrada
    try:
        numero = int(
            input("Introduzca el número entero del que quiera averiguar si es primo o no: "))
        primo = True
    # Proceso
        # El numero uno solo puede dividirse entre sí mismo, pero no se considera primo
        # Si el numero introducido es 1 cambiaremos primo a falso
        if numero == 1:
            primo = False

        # Asignamos a x el rango de numeros comenzaremos siempre por 2 puesto que todos los numeros son divisibles por 1
        # el contenido del rango será de 2 hasta un numero anterior del numero introducido
        # ejemplo con 7 (2,3,4,5,6)
        x = range(2, numero)
        # En el bucle for calculamos si alguno de los numeros de la lista al dividirlo entre numero da como resto 0
        # en caso de que algun resto sea 0 no será primo
        for n in x:
            resultado = numero % n
            if resultado == 0:
                primo = False

    # Salida
        # Si primo permanece verdadero mostraremos por pantalla que numero es primo
        if primo == True:
            print(numero, " es primo")
        # En caso contrario mostraremos por pantalla que numero no es primo
        else:
            print(numero, " no es primo")
    # Si no se introdujo un entero o hubo algun error inesperado, mostrará Error
    except:
        print("Error")
