import random

S = "Si"
N = "No"



IntentosMaximos = 4

while (True):
    x = int(random.randrange(10))    
    y = int(random.randrange(10))
    z = x * y        
        
    IntentosRealizados = 0

    for _ in range(IntentosMaximos):

        print(str(x) + "x" + str(y) + "= ")
        Num = int(input())            
        if(Num == z):
            print("Su respuesta es Correcta")
            break
        else:
            IntentosRealizados += 1
            intentosRestantes = IntentosMaximos - IntentosRealizados
            print("Su respuesta es Incorrecta repita su respuesta, tiene "+ str(intentosRestantes) + " intentos mas")
    else: 
        print("Se acabaron tus intentos, ¿desea continuar? (Si/No)")

        Respuesta = input()
        if (str.upper(Respuesta) == "SI" & "si" & ""):
            break
        if (str.upper(Respuesta) == "No"):
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
