# 10. Crea un un programa en Python que tome una lista de cadenas de caracteres
# y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal.
# La función debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.
def EjercicioPython10ListaVocal():
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
            list2 = []
            # Creamos la variable de control Peques y la asignamos a True
            Peques = True
            for x in input_list:
                # Comprobamos si alguna de las vocales se encuentran en cada elemento de la lista de input_list
                for i in "a", "e", "i", "o", "u":
                    if i in x.lower():
                        # Asignamos Peques a False
                        Peques = False
                        # Añadimos el elemento a list2 y realizamos un break, de lo contrario si tiene mas vocales añadiria la misma palabra varias veces
                        list2.append(str(x))
                        break
            # Si no se introdujo ningún valor con vocales
            if Peques == True:
                print("No se introdujo ninguna cadena con vocales ")
            # Si se introdujeron valores Peques deberia contener Falso, asi que mostramos lista2
            else:
                print("La lista resultante es:", list2)
        # Si el usuario no llegó a introducir ni un solo valor, self_destruct seguirá siendo True y mostrará un mensaje
        else:
            print("No has introducido nada :( ")

    except:
        print("Error")
