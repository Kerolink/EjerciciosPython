def Ejercicio2Salarios():
    # Entrada
    # Hacemos que el usuario introduzca todos los valores a calcular, lo transformamos a float al introducirlos, float acepta decimales y enteros
    try:
        salarioBase = float(input("Introduzca el salario base: "))
        pagasExtras = float(input("Introduzca las pagas extras: "))
        complementos = float(input("Introduzca los complementos: "))
        otrosConceptosRetributivos = float(
            input("Introduzca otros conceptos retributivos: "))
        IRP = float(input("Introduzca el IRP: "))
        seguridadSocial = float(input("Introduzca la seguridad social: "))
        # Proceso
        # Se realizan las operaciones necesarias y las asignamos a variables
        salarioBruto = salarioBase+pagasExtras+complementos+otrosConceptosRetributivos
        deducciones = IRP+seguridadSocial
        salarioNeto = salarioBruto-deducciones
        # Salida
        # Mostramos las variables salarioBruto y salarioNeto por la pantalla
        print("El salario Bruto es: ", salarioBruto)
        print("El salario Neto es: ", salarioNeto)
    except:
        print("Error, se detectaron valores no numéricos ")
