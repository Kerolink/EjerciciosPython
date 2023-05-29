# 2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona.
#   El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.
def EjercicioPython2TimeZone():
    from zoneinfo import ZoneInfo
    from datetime import datetime
    try:
        # Asignamos a user_input el valor introducido por el usuario
        user_input = input(
            "Nuestra zona horaria es Europe/Madrid. Introduzca su zona horaria: ")
        # Asignamos a time_zone :
        time_zone = ZoneInfo(user_input)
        # that makes the datetime object, we can then use the datetime object to print out the date and time
        dt = datetime.now(time_zone)
        print(time_zone)
        # will dump  out the date and time
        print(dt.isoformat())
        # Mostrará la hora actual en esa zona
        print(dt.timetz().isoformat())
    # Si no se introduce una zona horaria válida dará error
    except:
        print("Zona horaria ingresada no válida ")
