import os
from Ejercicio1DNI import Ejercicio1DNI
from Ejercicio2Salarios import Ejercicio2Salarios
from Ejercicio4Circulo import Ejercicio4Circulo
from Ejercicio5MayorYMenor import Ejercicio5MayorYMenor
from Ejercicio6Fahrenheit import Ejercicio6Fahrenheit
from Ejercicio7Par import Ejercicio7Par
from Ejercicio8Bisiesto import Ejercicio8Bisiesto
from Ejercicio9Palindromo import Ejercicio9Palindromo
from Ejercicio10Alfabetico import Ejercicio10Alfabetico
from Ejercicio11Factorial import Ejercicio11Factorial
from Ejercicio12Primo import Ejercicio12Primo
from Ejercicio13Cubo import Ejercicio13Cubo
from Ejercicio14SumaPar import Ejercicio14SumaPar
from Ejercicio15NegativoPositivoCero import Ejercicio15NegativoPositivoCero
from Ejercicio16Media import Ejercicio16Media
from Ejercicio17AdivinaNumero import Ejercicio17AdivinaNumero
from Ejercicio18Anagrama import Ejercicio18Anagrama
from Ejercicio19Duplicados import Ejercicio19Duplicados
from Ejercicio20Capicua import Ejercicio20Capicua

from EjercicioPython1YearFirst import EjercicioPython1YearFirst
from EjercicioPython2TimeZone import EjercicioPython2TimeZone
from EjercicioPython3CadenaWhile import EjercicioPython3CadenaWhile
from EjercicioPython4Horas import EjercicioPython4Horas
from EjercicioPython5InversoFor import EjercicioPython5InversoFor
from EjercicioPython6SumaFor import EjercicioPython6SumaFor
from EjercicioPython7CadenaLineaSeparada import EjercicioPython7CadenaLineaSeparada
from EjercicioPython8ListaFor import EjercicioPython8ListaFor
from EjercicioPython9Replace import EjercicioPython9Replace
from EjercicioPython10ListaVocal import EjercicioPython10ListaVocal
from EjercicioPython11Multiplo3 import EjercicioPython11Multiplo3

while True:
    os.system("cls")  # Limpia la pantalla cada vez que se vuelve al menú
    print("Bienvenido/a al Menú principal. Este programa recoge todos los ejercicios de Python. Seleccione el ejercicio que desea usar de la lista.")
    print("1 - Cálculo de letra DNI.")
    print("2 - Cálculo del salario")
    print("4 - Área y perímetro de un círculo")
    print("5 - Ordenación de números enteros.")
    print("6 - Conversor de Farenheit a Celsius")
    print("7 - Determinar si un número es par o impar")
    print("8 - Determinar si un año es bisiesto")
    print("9 - Saber si un texto es un palíndromo")
    print("10 - Ordenar alfabéticamente")
    print("11 - Cálculo de factoriales.")
    print("12 - Saber si un número es primo")
    print("13 - Volumen de un cubo")
    print("14 - Suma de números pares")
    print("15 - Saber si un número es positivo, negativo o 0.")
    print("16 - Cálculo de medias")
    print("17 - Juego de número aleatorio")
    print("18 - Saber si dos textos son anagramas.")
    print("19 - Eliminar números duplicados")
    print("20 - Determinar si un número es capicúa")

    print("21 - Ejercicio Python YearFirst")
    print("22 - Ejercicio Python TimeZone")
    print("23 - Ejercicio Python CadenaWhile")
    print("24 - Ejercicio Python Horas")
    print("25 - Ejercicio Python InversoFor")
    print("26 - Ejercicio Python SumaFor")
    print("27 - Ejercicio Python CadenaLineaSeparada")
    print("28 - Ejercicio Python ListaFor")
    print("29 - Ejercicio Python Replace")
    print("30 - Ejercicio Python ListaVocal")
    print("31 - Ejercicio Python Multiplo3")

    try:
        opcion = int(input(
            "Introduzca el número del algoritmo que quiere usar o introduzca 0 para cerrar el programa: "))

    except Exception:
        print("No ha seleccionado un ejercicio válido")

    if opcion == 0:
        input("Gracias por usar el programa. Pulse ENTER para salir.")
        break
    elif opcion == 1:
        Ejercicio1DNI()
    elif opcion == 2:
        Ejercicio2Salarios()
    elif opcion == 4:
        Ejercicio4Circulo()
    elif opcion == 5:
        Ejercicio5MayorYMenor()
    elif opcion == 6:
        Ejercicio6Fahrenheit()
    elif opcion == 7:
        Ejercicio7Par()
    elif opcion == 8:
        Ejercicio8Bisiesto()
    elif opcion == 9:
        Ejercicio9Palindromo()
    elif opcion == 10:
        Ejercicio10Alfabetico()
    elif opcion == 11:
        Ejercicio11Factorial()
    elif opcion == 12:
        Ejercicio12Primo()
    elif opcion == 13:
        Ejercicio13Cubo()
    elif opcion == 14:
        Ejercicio14SumaPar()
    elif opcion == 15:
        Ejercicio15NegativoPositivoCero()
    elif opcion == 16:
        Ejercicio16Media()
    elif opcion == 17:
        Ejercicio17AdivinaNumero()
    elif opcion == 18:
        Ejercicio18Anagrama()
    elif opcion == 19:
        Ejercicio19Duplicados()
    elif opcion == 20:
        Ejercicio20Capicua()
    elif opcion == 21:
        EjercicioPython1YearFirst()
    elif opcion == 22:
        EjercicioPython2TimeZone()
    elif opcion == 23:
        EjercicioPython3CadenaWhile()
    elif opcion == 24:
        EjercicioPython4Horas()
    elif opcion == 25:
        EjercicioPython5InversoFor()
    elif opcion == 26:
        EjercicioPython6SumaFor()
    elif opcion == 27:
        EjercicioPython7CadenaLineaSeparada()
    elif opcion == 28:
        EjercicioPython8ListaFor()
    elif opcion == 29:
        EjercicioPython9Replace()
    elif opcion == 30:
        EjercicioPython10ListaVocal()
    elif opcion == 31:
        EjercicioPython11Multiplo3()
    else:
        "No ha seleccionado un número correcto"
    input("Pulsa Enter para continuar.")
