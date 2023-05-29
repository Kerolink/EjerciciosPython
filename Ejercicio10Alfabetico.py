def Ejercicio10Alfabetico():
    # Entrada
    # Creamos la lista y las variables de control
    input_list = []
    loop = True
    self_destruct = True
    # Proceso
    try:
        # Mientras loop sea True preguntaremos al usuario si quiere anadir palabras
        while loop == True:
            user_input = input(
                "Añade una palabra a la lista, no añada nada para dejar de añadir palabras: ")
            # Si no se introduce nada loop cambia a False y se cierra el bucle
            if user_input == "":
                loop = False
            # Si se introduce una palabra se asigna al final de la lista de input_list
            else:
                input_list.append(str(user_input))
                # Tambien asignaremos self_destruct False
                self_destruct = False
        # Salida
        # Si al menos se introdujo un valor mostraremos la lista ordenada alfabéticamente
        if self_destruct == False:
            print(
                "A continuación aparecen las palabras que a introducido por orden alfabético: ")
            print(sorted(input_list))
        # Si el usuario no llegó a introducir ni un solo valor, self_destruct seguirá siendo True y mostrará un mensaje
        else:
            print("No has introducido nada :( ")

    except:
        print("Error")
