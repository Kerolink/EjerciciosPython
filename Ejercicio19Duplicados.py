def Ejercicio19Duplicados():
    # Entrada
    # Asignamos a input_list una lista con duplicados
    input_list = list([2, 5, 7, 9, 7, 73, 4, 2, 5, 8])
    # Asignamos a la variable i 0
    i = 0
    # Proceso

    # El bucle se repetirá mientras i sea menor que la longitud de la lista
    while (i < len(input_list)):
        # Asignamos a la variable j el valor que contenga i + 1
        j = i+1
        # Mientras j sea menor que la longitud de la lista
        while (j < len(input_list)):
            # si el valor de la posicion i de input_list es igual al valor de su posición j
            if input_list[i] == input_list[j]:
                # elimina el valor de su posición j
                del input_list[j]
            # de lo contrario asignaremos a j el valor de j + 1
            else:
                j = j + 1
        # Asignamos a i el valor de i + 1
        i = i + 1

    # Salida
    print(input_list)
