def juego():
    num1 = int(input("Elige un numero del 1 al 100: "))
    num2=58
    x=0
    while True: 
        if (num1 == num2):
            break
        else: 
            x = x + 1
            print("Incorrecto. Intenta de nuevo:")
            num1 = int(input("Elige nuvamente: "))
    
    print("¡Correcto! Adivinaste el número después de", x, "intentos.")
    input()


def Calculadora(): 
    print("Calculadora")
    print("***********")
    num1 = int(input("Ingrese primer número: "))
    num2 = int(input("Ingrese segundo número: "))
    print("Operaciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    operacion = int(input("Ingrese el número de la operación: "))
    if(operacion == 1):
            suma = num1 + num2
            print("La suma de estos dos números es: " + str(suma))
    elif(operacion == 2):
            resta = num1 - num2
            print("La resta de estos dos números es: " + str(resta))
    elif(operacion == 3):
            multiplicacion = num1 * num2
            print("La multiplcación de estos dos números es: " + str(multiplicacion))
    elif(operacion == 4):
            division = num1 // num2
            print("La division de estos dos números es: " + str(division))
    input()


def tabla_de_multiplicar():
    print("Tablas de multiplicar")
    num = int(input("Ingrese la tabla de multiplicar que quiera: "))
    print("Tabla de multiplicar del " + str(num))
    for x in range(1, 11):
        resultado = num * x
        print(str(num) + " x " + str(x) + " = " + str(resultado))
    input()


def convertir_unidades():
    print("Conversor de Unidades")
    print("1. Kilómetros a Millas")
    print("2. Millas a Kilómetros")
    opcion1 = int(input("Selecciona una opción (1 o 2): "))
    if (opcion1 == 1):
        num1 = float(input("Ingrese la medida en kilometros: "))
        Millas = num1 * 0.621371
        print(str(num1) + " en Millas es: " + str(Millas))
    elif (opcion1 == 2):
        num2 = float(input("Ingrese la medida en Millas: "))
        kilometro = num2 * 1.60934
        print(str(num2) + " en Kilometros es: " + str(kilometro))
    else:
         print("Opción no válida")        
    input()


def gran_suma():
    print("¿Cuantos numeros va a sumar?")
    num1 = int(input())
    x=0
    suma = 0
    while x<num1:
        num2 = int(input("Ingrese el número " + str(x + 1) + ": "))
        suma = suma + num2
        x=x+1
    promedio = suma/num1
    print("La suma de todos los numero es: " + str(suma))
    print("El promedio total de todo estos numero es: " + str(promedio))
    input()
      

def Menu():        
    print("Menu:")
    print("1. Juego")
    print("2. Calculadora")
    print("3. Tablas de Multiplicar")
    print("4. Conversor de Unidades")
    print("5. Suma Grande")   
    opcion = input("Ingrese una opción (1 al 5): ")
    if opcion == "1":
        juego()
    elif opcion == "2":
        Calculadora()
    elif opcion == "3":
        tabla_de_multiplicar()
    elif (opcion == "4"):
        convertir_unidades()
    elif (opcion == "5"):
        gran_suma()
    else:
            print("Opción no válida")        
            
Menu()