# Este es el juego de adivinar el número.

"""1"""import random
"""2"""intentosRealizados = 0
"""3"""print('¡Hola! ¿Cómo te llamas?')
"""4"""miNombre = input()
"""5"""número = random.randint(1, 20)
"""6"""print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')
"""7"""while intentosRealizados < 6:
"""8"""    print('Intenta adivinar.') # Hay cuatro espacios delante de print.
"""9"""    estimación = input()
"""10"""    estimación = int(estimación)
"""11"""    intentosRealizados = intentosRealizados + 1
"""12"""    if estimación < número:
"""13"""        print('Tu estimación es muy baja.') # Hay ocho espacios delante de print.
"""14"""    if estimación > número:
"""15"""        print('Tu estimación es muy alta.')
"""16"""    if estimación == número:
"""17"""        break
"""18"""if estimación == número:
"""19"""    intentosRealizados = str(intentosRealizados)
"""20"""    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')
"""21"""if estimación != número:
"""22"""    número = str(número)
"""23"""    print('Pues no. El número que estaba pensando era ' + número)
