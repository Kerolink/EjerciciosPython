# 4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo,
# "19:30" se convertiría en "19:30").
#   La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.
# from datetime import datetime
# Con el ejercicio No. 4 deberas contemplar:
# Variables de control
def EjercicioPython4Horas():
    am = False
    pm = False
    seguir = True
    try:
        # 1 – La entrada: El usuario pone una hora en un formato determinado: "hh:mm".
        userHour = input("Introduzca la hora en formato hh:mm por favor: ")
        # Troceamos la hora para trabajar con ella
        HoraTroceada = userHour.split(":")
        # La separamos en diferentes variables
        Hora = HoraTroceada[0]
        Minutos = HoraTroceada[1]
        # Las convertimos a enteros
        Hora = int(Hora)
        Minutos = int(Minutos)
        # Si la hora es un número negativo o superior a 24 mostraremos un error y asignaremos False a seguir
        if Hora < 0 or Hora > 24:
            print("Introdujo una hora incorrecta ")
            seguir = False
        # Si los minutos son un número negativo o superior a 60 mostraremos un error y asignaremos False a seguir
        if Minutos < 0 or Minutos > 60:
            print("Introdujo los minutos incorrectamente ")
            seguir = False
        # Si la hora es menor o igual a doce preguntaremos al usuario si es de la mañana o de la tarde
        if Hora <= 12:
            control = input("Introduzca si es de la mañana o de la tarde: ")
            # Si es de la mañana asignaremos a am True
            if control.lower() == "am" or control.lower() == "mañana":
                am = True
                pm = False
            # Si es de la tarde asignaremos a pm True
            if control.lower() == "pm" or control.lower() == "tarde":
                pm = True
                am = False

        # 2 – El Proceso: A partir de la hora que el usuario ha puesto realizará un calculo y la convertirá en 24 horas

        # 3 - Si no está en ese formato no deberías convertir la hora a 24 horas
        # Si seguir es True ...
        if seguir == True:
            # Si la hora es mayor a 12 mostraremos por la pantalla userHour
            if Hora > 12:
                print(userHour)
                print("Son las:", Hora, "y", Minutos, "minutos ")
            # Si la hora es menor o igual a 12 ...
            if Hora <= 12:
                # Si am es True ...
                if am == True:
                    # Si la hora es 12 am Mostraremos que es 0 (am)
                    if Hora == 12:
                        print("0", ":", Minutos)
                        print("Son las 0", "y", Minutos, "minutos ")
                    # De lo contrario mostraremos userHour
                    else:
                        print(userHour)
                        print("Son las:", Hora, "y", Minutos, "minutos ")
                # Si pm es True ...
                if pm == True:
                    # Asignamos a la variable result el resto de dividir el resultado de la suma Hora + 12
                    result = (Hora + 12) % 24
                    # Si el resto es 0 diremos que son las 12 (pm)
                    if result == 0:
                        print("12", ":", Minutos)
                        print("Son las 12", "y", Minutos, "minutos ")
                    # De lo contrario la hora sera result y lo mostraremos por la pantalla
                    else:
                        print(result, ":", Minutos)
                        print("Son las", result, "y", Minutos, "minutos ")

        # 4 - Si el usuario pone 19:30 ya está en formato 24 horas, por lo que el calculo ya esta hecho (19:30)

        # 5 - Si el usuario pone 7:23 no está en 24 hora, lo que deberá calcular cual es esa hora y pasarla a 19:23.

        # 6 – La salida: Mostrar la Hora calculada.

        # Me imagino que tu duda viene por el tema de que pasa se quiere poner 7:30 en la mañana o 7:30 en la tarde.

        # Deberás inclurir en la entrada una pregunta si es AM o PM para incluir este escenario. (Horas menores de 12:00)
    except:
        print("Error")
