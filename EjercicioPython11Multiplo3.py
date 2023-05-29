# 11. Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3.
#    El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar los números.

# Lo que buscamos aquí es que al dividir el número entre el otro, el residuo sea cero.
# Para sacar el residuo de una división en Python usamos el operador módulo %
def EjercicioPython11Multiplo3():
    # Entrada
    # Creamos la lista y las variables de control
    input_list = []
    loop = True
    self_destruct = True
    list2 = []
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

        # Para cada valor de la lista
        for x in input_list:
            if x % 3 == 0:
                list2.append(int(x))
                # Salida
                # Si al menos se introdujo un valor mostraremos
        if self_destruct == False:
            print("La lista de numeros que ha introducido es la siguiente: ")
            print(input_list)
            print("Los números múltiplos de 3 de esa lista son: ")
            print(list2)
            # Si el usuario no llegó a introducir ni un solo número, self_destruct seguirá siendo True y mostrará un mensaje
        else:
            print("No introdujiste nada :( ")
        # El programa dará error si el usuario no introduce numeros enteros
    except:
        print("Error")
