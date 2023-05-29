# 1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"`
# y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero.
# El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.

def EjercicioPython1YearFirst():
# from datetime import date
    try:
        # Asignamos a fechaUsuario el valor introducido por el usuario deberá ser en el formato especificado por el programa
        fechaUsuario = input("Introduzca una fecha en formato dd/mm/aaaa: ")

        # Dividimos los valores de la cadena fechaUsuario y lo asignamos a x
        x = fechaUsuario.split("/")
        # Solucionador de Errores:  #Si alguno no fuera un numero entero saltaría al except
        PosibleError0 = int(x[0])  # Dia
        PosibleError1 = int(x[1])  # Mes
        PosibleError2 = int(x[2])  # Año
        # Si la longitud de x es igual a 3, y PosibleError0 es mayor a 0 y menor o igal a 31, y PosibleError1 es mayor a 0 y menor o igual a 12 entonces
        if len(x) == 3 and PosibleError0 <= 31 and PosibleError1 <= 12 and PosibleError0 > 0 and PosibleError1 > 0:
            # date(year, month, day)
            # date(x[2],x[1],x[0])
            # Mostramos por la pantalla x[2] valor en la posición del año, / x[1] valor en la posición del mes / x[0] valor en la posición del día
            print(x[2], "/", x[1], "/", x[0])
        # Si no se introdujo la cantidad adecuada de valores
        else:
            print(
                "No tiene la cantidad de valores adecuada o introdujo un día o mes imposibles")
    # Habra un error a no ser que el usuario introduzca la fecha correctamente
    except:
        print("No introdujsiste el formato exigido ")
