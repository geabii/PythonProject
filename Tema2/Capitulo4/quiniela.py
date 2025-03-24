print('¡Hola! ¿Cómo te llamas?')
miNombre = input()
print('Bueno, ' + miNombre + ', vamos a generar los resultados de los 15 partidos')

import random

for i in range(1,16):
    numero=random.randint(1,3)
    if numero==1:
        resultado='1'
    if numero==2:
        resultado='2'
    if numero==3:
        resultado='x'
    print('Partido '+ str(i)+' El resultado será '+resultado)
