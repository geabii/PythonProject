#Elegimos la palabra oculta
palabra = "oculto"

#Ahora la letra que introducirá el usuario
letra_introducida = input('Introduce una letra: ').lower

#Hacemos la comprobación de si la letra introducida está dentro de la palabra oculta
if letra_introducida in palabra:
        print('Tu letra SÍ está dentro de la palabra oculta.')
else:
        print('Tu letra NO está dentro de la palabra introducida')
