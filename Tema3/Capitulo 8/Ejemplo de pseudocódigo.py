#Elegimos la palabra oculta
palabra = "oculto"

#Ahora la letra que introducirá el usuario
while True:

    letra_introducida = input("Introduce una letra(introduzca la palabra 'salir' para salir del programa: ").lower()

#Hacemos la comprobación de si la letra introducida está dentro de la palabra oculta
    if letra_introducida in palabra:
            print("Tu letra SÍ está dentro de la palabra oculta.")

    elif letra_introducida == 'salir':
        break


    else:
            print("Tu letra NO está dentro de la palabra introducida")

    if letra_introducida == palabra:
        print('Enhorabuena, usted a adivinado la palabra')
        break

