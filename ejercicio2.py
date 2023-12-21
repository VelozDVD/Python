while True:
    Nombre = input("Escribe tu nombre: ").capitalize()
    if not Nombre.isalpha():
        print("Ingrese su nombre correctamente")
    else: 
        break
print("Hola " + str(Nombre) + ", ¿Como estas?")
print("¿Que deporte te gusta mas?")
print("Futbol")
print("Basquet")
while True:
    while True:
        Deporte = input("Ingresa el deporte: ").capitalize()
        if not Deporte.isalpha():
            print("Ingrese su nombre correctamente")
        else:
            break
    if(Deporte == "Futbol" or Deporte == "Basquet"):
        break
    else:
        print("Ingrese un valor valido")
print("Muy buen deporte! El " + Deporte + " es uno de los mejores deportes de todos los tiempos")
input()
print(Nombre + " eres una persona muy inteligente, ahora vamos a jugar algo de matematicas")
y = 4
z = 3 
Intentos = 0
for Intentos in range(z):
    x = int(input("Cuanto es: 2 + 2: "))
    if(x == y):
        print("Muy bien la respuesta es: " + str(x) + "!!")
        break
    else:
        Intentos += 1
        print("No... eres un pendejo")
        if(Intentos < z):
            print("Te quedan " + str(z - Intentos) + " piensa bien tu respuesta crvrg")
        else:
            print("Se te acabaron los intentos. La respuesta correcta era 4.")
            break

print("Bueno... veo que eres super pilas, que tal si ahora jugamos a adivinar el numero")
print("Es un numero del 1 al 10")
Respuesta = 6
numIntentos = 0 
o = 3
for numIntentos in range(o):
    intento = int(input("Ingresa el numero que creas: "))
    numIntentos += 1
    if(intento == Respuesta):
        print("Muy bien lo lograste!")
        print("Solo te tomo " + str(numIntentos) + " intentos")        
        break
    else:        
        print("No esta mal :(")
        if(numIntentos < o):
            print("Te quedan " + str(o - numIntentos) + " intentos")
        else:
            print("Ya valio, mejor suerte la proxima")
            break

# z = 0
# while True:
#     z += 1
#     print(str(z))
#     if(z == 100):
#         break

    

