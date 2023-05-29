# 6. Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado.
#    El programa debe utilizar un bucle `for` para sumar los números.

def EjercicioPython6SumaFor():
    try:
        # Pedimos un numero al usuario y lo asignamos a la variable numero
        numero = int(input("Introduzca un número entero: "))
        Suma = 0
        for x in range(numero+1):
            # Con el if nos saltamos el 0
            if x != 0:
                Suma = Suma+x
        print("El resultado de la suma de la suma desde 1 hasta", numero, "es", Suma)
    # El programa mostrará error si no se introduce un número entero
    except:
        print("No introdujiste un número entero")
