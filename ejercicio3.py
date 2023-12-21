print("Ls Clothes")
print("__________")

# Saludar al usuario
nombre = input("Ingrese tu nombre: ")
apellido = input("Ingresa tu apellido: ")

print("Hola, " + nombre + " " + apellido + "!" + " Bienvenido a Ls Clothes!")
print("____________________________________________________________________")

# Pregunta de la tienda
print("¿Qué desea comprar en nuestra tienda?")
# Opciones que ofrece la tienda
print("Chompa: $20")
print("Camisa: $10")
print("Medias: $5.50")
print("Zapatos: $35.99")

# Escoger las opciones
clave = "NO"
entrada = ""
Chompa = 0
Camisa = 0
Medias = 0
Zapatos = 0

while entrada != clave:

    print("Escoga las prendas que desea: ")
    print("Si desea cancelar la compra escriba: (cancelar)")
    palabra = input()

    if palabra == "Chompa":
        Chompa = 20
    if palabra == "cancelar":
        break
    if palabra == "Camisa":
        Camisa = 10
    if palabra == "cancelar":
        break
    if palabra == "Medias":
        Medias = 5.50
    if palabra == "cancelar":
        break
    if palabra == "Zapatos":
        Zapatos = 35.99
    if palabra == "cancelar":
        break
    print("¿Desea agregar algo más? SI/NO")
    entrada = input()

Suma = Chompa + Camisa + Medias + Zapatos

print("El total es:", Suma)

Iva = Suma * 0.12

print("El total más IVA es:", Suma + Iva)

print("El día de hoy estamos con descuento, pero si quieres tu descuento tendrás que elegir un color")

print("Seleccione un Color, para aplicar su descuento")
print("1. Amarillo")
print("2. Rojo")
print("3. Blanco")

opcion = int(input("Opción: "))
resultado = Suma

if opcion == 1:
    resultado = -Suma * 25 / 100 + Suma
elif opcion == 2:
    resultado = -Suma * 40 / 100 + Suma
elif opcion == 3:
    print("No obtiene descuento :,(")
else:
    print("Opción inválida.")

Iva2 = resultado * 0.12

print("El total con descuento es:", resultado + Iva2)

input("¿Desea agregar un comentario?")

print("Muchas gracias por su comentario")
