import random

S = "Si"
N = "No"

while True:
    Nombre = input("Hola, ¿Comó te llamas?: ").capitalize()
    if not Nombre.isalpha():
        print("Ingresa correctamente tu nombre: ")
    else:
        break

print("Hola " + Nombre + ", ¡Bienvenido al juego de las tablas!")
print("Comenzemos!")
IntentosMaximos = 4

while (True):
    x = int(random.randrange(10))    
    y = int(random.randrange(10))
    z = x * y        
        
    IntentosRealizados = 0

    for _ in range(IntentosMaximos):

        print(str(x) + "x" + str(y) + "= ")
        Num = input()            
        if(Num == z):
            print("Su respuesta es Correcta")
            break
        if not Num.isalpha():
            print("Ingrese un número valido")
        if(Num != int()):
            print("Ingrese un número valido")
        else:
            IntentosRealizados += 1
            intentosRestantes = IntentosMaximos - IntentosRealizados
            print("Su respuesta es Incorrecta repita su respuesta, tiene "+ str(intentosRestantes) + " intentos mas")
    else: 
        print("Se acabaron tus intentos, ¿desea continuar? (Si/No)")

        Respuesta = input().capitalize()
        if (Respuesta == "Si"):
            break
        # elif(Respuesta == None):

        if (Respuesta == "No"):
            print("Sigue Practicando")
            sys.exit()
            
    




# import random

# IntentosMaximos = 4

# while True:
#     x = int(random.randrange(10))    
#     y = int(random.randrange(10))
#     z = x * y        
#     IntentosRealizados = 0

#     for _ in range(IntentosMaximos):

#         print(str(x) + "x" + str(y) + "= ")
#         Num = int(input())            
#         if Num == z:
#             print("Su respuesta es Correcta")
#             break
#         else:
#             IntentosRealizados += 1
#             intentosRestantes = IntentosMaximos - IntentosRealizados
#             print("Su respuesta es Incorrecta. Le quedan " + str(intentosRestantes) + " intentos.")

#     else:
#         print("Ha agotado todos los intentos. La respuesta correcta era " + str(z))
    
#     continuar = input("¿Desea jugar de nuevo? (s/n): ")
#     if continuar.lower() != 's':
#         break
