# 9. Crea un programa en Python donde la entrada sean una cadena de caracteres, una palabra y una palabra de reemplazo ,
# el resultado debe ser la cadena con todas las ocurrencias de la palabra reemplazadas por otra palabra.
#   El programa debe utilizar un bucle `while` para buscar todas las ocurrencias de la palabra y reemplazarlas.
def EjercicioPython9Replace():
    # Asignamos a input_string la cadena introducida por el usuario
    input_string = input("Introduzca una cadena de caracteres: ")
    # Asignamos a WordWantReplace el valor que el usuario quiere reemplazar
    WordWantReplace = input("¿Qué valor te gustaría reemplazar?: ")
    # Asignamos a Replacement el valor que el usuario quier colocar en lugar del valor indicado en WordWantReplace
    Replacement = input("¿Por qué valor te gustaría reemplazarlo?: ")
    # Troceamos input_string y lo asignamos a cadena
    cadena = input_string.split()
    i = 0
    cadenAntes = " ".join(cadena)
    print("La cadena antes del reemplazo:", cadenAntes)

    # Mientras i no sea igual a la longitud de cadena
    while i != len(cadena):

        # Si el valor de cadena en la posición i es igual a WordWantReplace
        if cadena[i] == WordWantReplace:
            # Sustituiremos ese valor por lo asignado en Replacement
            cadena[i] = Replacement
        i = i+1

    cadenaDespues = " ".join(cadena)
    print("La cadena tras el reemplazo:", cadenaDespues)
