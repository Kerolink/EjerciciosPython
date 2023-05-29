def Ejercicio1DNI():
    # Ejercicio CalculoDNI
    # Entrada
    # Asignamos a la variable tablaLetrasDNI la lista de letras y creamos la variable resultado
    tablaLetrasDNI = 'TRWAGMYFPDXBNJZSQVHLCKE'

    # Creamos un try con la entrada del DNI y todo el proceso
    try:
        # El usuario introduce un DNI por el teclado, se le considerará una cadena por el momento
        DNI = input("Introduzca el número del DNI: ")
        # Proceso
        # Si la longitud de la cadena DNI es de 8 transformaremos DNI en un integer
        if len(DNI) == 8:
            DNI = int(DNI)
        # Obtenemos el resto de dividir el DNI entre 23, con la funcion [] cogeremos la letra de la posicion que sea igual al del resto obtenido
        # Con print mostramos por la pantalla
            print('La letra del DNI es: ', tablaLetrasDNI[DNI % 23])
            print(f"El DNI completo sería: {DNI}{tablaLetrasDNI[DNI%23]}")
        # Si la longitud de DNI no es 8 no es un DNI y lo mostraremos por la pantalla
        else:
            print("Eso no es un DNI ")
    # Si algo fue mal, por ejemplo si DNI contenía una cadena de 8 letras en lugar de números, también mostraremos que no es un DNI
    except:
        print('Eso no es un DNI ')
