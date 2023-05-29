def Ejercicio5MayorYMenor():

    # Entrada
    # Creamos las variables; a Mayor le asignamos un valor valor bajo
    Mayor = 0
    # Y con Menor asignamos un valor enorme
    Menor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    # Creamos la lista y las variables de control
    input_list = []
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
                input_list.append(float(user_input))
                # Tambien asignaremos self_destruct False
                self_destruct = False

        # Para cada valor de la lista, compararemos si es mayor o menor
        for x in input_list:
            # Si x es mayor que Mayor asignamos a Mayor el valor de x
            if x > Mayor:
                Mayor = x
            # Si x es menor que Menor asignamos a Menor el valor de x
            # Aqui habría problemas si iniciamos ambas variables a 0 porque ningun numero es menor a 0
            if x < Menor:
                Menor = x

        # Salida
        # Si al menos se introdujo un valor mostraremos Mayor y Menor
        if self_destruct == False:
            print("El número mayor es", Mayor)
            print("El número menor es", Menor)
        # Si el usuario no llegó a introducir ni un solo número, self_destruct seguirá siendo True y mostrará un mensaje
        else:
            print("No introdujiste nada :( ")
    # El programa dará error si el usuario introduce letras o espacios en lugar de numeros
    except:
        print("Error")
