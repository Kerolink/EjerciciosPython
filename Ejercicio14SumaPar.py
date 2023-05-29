def Ejercicio14SumaPar():
    # Entrada
    # Creamos la lista y las variables de control
    input_list = []
    Par = 0
    loop = True
    self_destruct = True
    # Proceso
    try:
        # Mientras loop sea True preguntaremos al usuario si quiere anadir numeros
        while loop == True:
            user_input = input(
                "Añade un número a la lista, no añada nada para dejar de añadir números: ")
            # Si no se introduce nada loop cambia a False y se cierra el bucle
            if user_input == "":
                loop = False
            # Si se introduce un numero se asigna al final de la lista de input_list
            else:
                input_list.append(int(user_input))
                # Tambien asignaremos self_destruct False
                self_destruct = False

        # Para cada valor de la lista, y su resto es 0 al dividirlo entre 2 que indica que es par ...
        for x in input_list:
            if x % 2 == 0:
                # Le asignaremos a Par la suma entre Par y x
                Par = Par+x
        # Salida
        # Si al menos se introdujo un valor mostraremos
        if self_destruct == False:
            print("La lista de numeros que ha introducido es la siguiente: ")
            print(input_list)
            print("El resultado de los numeros pares es: ", Par)
            # Si el usuario no llegó a introducir ni un solo número, self_destruct seguirá siendo True y mostrará un mensaje
        else:
            print("No introdujiste nada :( ")
        # El programa dará error si el usuario no introduce numeros enteros
    except:
        print("Error")
