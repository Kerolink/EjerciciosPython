# 7. Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada.
#   El programa debe utilizar un bucle `for` para recorrer la cadena.
def EjercicioPython7CadenaLineaSeparada():
    # Asignamos a cadena el valor introducido por el usuario
    cadena = input("Introduzca una cadena de caracteres: ")
    print(cadena, "se compone de: ")
    # El bucle for recorrerá cada caracter de cadena y lo mostrará por la pantalla, cada iteración en una linea distinta
    for x in cadena:
        print(x)
