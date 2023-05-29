# 8. Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen
# más de 5 caracteres.
#   El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.
def EjercicioPython8ListaFor():
    # Creamos la lista y las variables de control
    input_list = []
    loop = True
    self_destruct = True
    # Proceso
    try:
        # Mientras loop sea True preguntaremos al usuario si quiere anadir cadenas de caracteres
        while loop == True:
            user_input = input(
                "Añade una cadena de caracteres a la lista, no añada nada para dejar de añadir: ")
            # Si no se introduce nada loop cambia a False y se cierra el bucle
            if user_input == "":
                loop = False
            # Si se introduce una palabra se asigna al final de la lista de input_list
            else:
                input_list.append(str(user_input))
                # Tambien asignaremos self_destruct False
                self_destruct = False
        # Salida
        # Si al menos se introdujo un valor
        if self_destruct == False:
            print("La lista que introdujo es:", input_list)
            print("Las cadenas con más de 5 caracteres son las siguientes:")
            # Creamos la variable de control Peques y la asignamos a True
            Peques = True
            for x in input_list:
                # Mediante la estructura de control if podemos saltarnos aquellas cadenas cuya longitud de caracteres sean igual o menor que 5
                if len(x) > 5:
                    # Asignamos Peques a False
                    Peques = False
                    print(x)
            # Si no se introdujo ningún valor mayor a 5 caracteres mostraremos un mensaje
            if Peques == True:
                print("No se introdujo ninguna cadena mayor a 5 caracteres ")
        # Si el usuario no llegó a introducir ni un solo valor, self_destruct seguirá siendo True y mostrará un mensaje
        else:
            print("No has introducido nada :( ")

    except:
        print("Error")
