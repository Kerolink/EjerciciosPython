# 5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh").
# El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.
def EjercicioPython5InversoFor():
    # Asignamos a la variable cadena el valor introducido por el usuario
    cadena = input("Introduzca una cadena para invertir: ")
    # Creamos la variable cadenaInvertida
    cadenaInvertida = ""

    # Recorremos la cadena invertida
    for x in reversed(cadena):
        # Asignamos a cadenaInvertida, el valor actual de cadenaInvertida y la letra que contenga x en ese paso
        cadenaInvertida = cadenaInvertida+x

    # cadenaInvertida = "".join(reversed(cadena)) Esta sentencia nos ahorraría el blucle for
    # Mostramos cadenaInvertida por la pantalla
    print(cadenaInvertida)
