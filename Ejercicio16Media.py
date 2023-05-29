def Ejercicio16Media():

    # Entrada
    # Creamos la lista y las variables de control
    input_list = []
    SumaTotal = 0
    Media = 0
    i = 0
    loop = True
    self_destruct = True
    # Proceso

    # Mientras loop sea True preguntaremos al usuario si quiere anadir numeros
    while loop == True:
        try:
            user_input = input(
                "Añade un número a la lista, no añada nada para dejar de añadir números: ")
            # Si no se introduce nada loop cambia a False y se cierra el bucle
            if user_input == "":
                loop = False
            # Si se introduce un numero se asigna al final de la lista de input_list
            else:
                input_list.append(float(user_input))
                # Tambien asignaremos self_destruct False
                self_destruct = False
        # El programa dará error si el usuario introduce letras o espacios en lugar de numeros
        except:
            print("Error entrada inválida")

    # Si al menos se introdujo un valor...
    if self_destruct == False:
        # Para cada valor de la lista,
        for x in input_list:
            # Asignamos a SumaTotal la suma de x y SumaTotal
            SumaTotal = SumaTotal+x
            # Asignamos a i la suma de i mas 1, esto indica el numero de valores introducidos
            i = i+1
            # Asignamos a Media la división de Sumatotal entre i
        Media = SumaTotal/i
    # Salida
        print("La lista de numeros que ha introducido es la siguiente: ")
        print(input_list)
        print("El resultado de la suma de los numeros es: ", SumaTotal)
        print("La media es: ", Media)
    # Si el usuario no llegó a introducir ni un solo número, self_destruct seguirá siendo True y mostrará un mensaje
    else:
        print("No introdujiste nada :( ")
