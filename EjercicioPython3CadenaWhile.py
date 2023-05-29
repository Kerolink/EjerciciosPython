# 3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene.
# El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.
def EjercicioPython3CadenaWhile():
    # Asignamos a la variable cadena la cadena introducida por el usuario
    cadena = input("Introduzca una cadena: ")
    # Separamos la cadena, el separador será el espacio
    cadenaSeparada = cadena.split()
    # Con len contamos las palabras de cadenaSeparada y lo asignamos a cantidadPalabras
    cantidadPalabras = len(cadenaSeparada)
    # Asignamos un par de nuevas variables el 0 para el control del bucle while
    numeroPalabras = 0
    i = 0
    # Mientras i sea distinto a cantidadPalabras
    while i != cantidadPalabras:
        # Muestra por la pantalla el numero i + 1 (Para que no empiece contando en 0) y la palabra que corresponde a la posición i actual
        print("La palabra numero", i+1, "es", cadenaSeparada[i])
        # Se le asigna a i el valor de i+1 en cada interacción, una vez i alcance a cantidadPalabras el buble terminará
        i = i+1
    # Mostramos cuantas palabras hay en total podriamos usar cantidadPalabras tambien
    print("Hay", i, "palabras en total")
