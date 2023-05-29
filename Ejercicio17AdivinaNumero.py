def Ejercicio17AdivinaNumero():
    # Entrada
    try:
        import random
        # Asignamos a randomNumber un número aleatorio entre 1 y 100
        randomNumber = random.randint(1, 100)
        # Asignamos a userNumber 0 no sera nunca igual a randomNumber en este punto
        userNumber = 0
        # Proceso
        # El bucle while se repetirá hasta que
        while userNumber != randomNumber:
            # Asignamos a userNumber el valor que introduzca el usuario
            userNumber = int(input("Adivine el número: "))
            # Si es menor que randomNumber se lo diremos por la pantalla
            if userNumber < randomNumber:
                print("Su número es menor del que tiene que adivinar ")
            # Si es mayor que randomNumber se lo diremos por la pantalla
            elif userNumber > randomNumber:
                print("Su número es mayor del que tiene que adivinar ")
        # Salida

        # Mostramos por la pantalla que lo adivinó
        print("¡Lo adivinaste!")
        # El programa podría fallar al intentar introducir letras, por ejemplo
    except:
        print("Error")
