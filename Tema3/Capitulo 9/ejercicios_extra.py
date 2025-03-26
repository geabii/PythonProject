import random

print('Elige una de las siguientes opciones del menú: \n 1 Sucesión de fibonacci. \n 2 Números primos del 1 al 100. \n 3 Introducir 3 números y ordenarlos. \n 4 Tirar dados. \n 5 Examen básico de 15 preguntas matemáticas.')
opcion = int(input('Selecciona la opción: '))
if opcion == 1:
    numeros = int(input("Introduce cuántos números quieres visualizar de la sucesión de Fibonacci: "))
    a = 0
    b = 1
    contador = 0
    while contador < numeros:
        print(a, end=", " if contador < numeros - 1 else "\n")
        # a sería igual a b para el siguiente numero y b sería la suma de a y b
        a = b
        b = a + b
        contador = contador + 1

elif opcion == 2:
    numero = 1
    while numero <= 100:
        divisor = 1
        divisores = 0
        while divisor <= numero:
            resultado = numero / divisor
            if resultado.is_integer():
                divisores = divisores + 1
            divisor = divisor + 1
        if divisores == 2:
            print(numero)
        numero = numero + 1

elif opcion == 3:
    numero1 = input('Introduce el primer número: ')
    numero2 = input('Introduce el segundo número: ')
    numero3 = input('Introduce el tercer número: ')
    print('Ahora vamos a ordenarlos de menor a mayor')
    if numero1 <= numero2 and numero2<= numero3:
        print(numero1, numero2, numero3)
    elif numero1 <= numero3 and numero3<= numero2:
        print(numero1, numero3, numero2)
    elif numero2 <= numero1 and numero1<= numero3:
        print(numero2, numero1, numero3)
    elif numero2 <= numero3 and numero3<= numero1:
        print(numero2, numero3, numero1)
    elif numero3 <= numero1 and numero1<= numero2:
        print(numero3, numero1, numero2)
    else:
        print(numero3, numero2, numero1)
elif opcion == 4:
    tiradas = int(input('Introduce el número de tiradas que quieres realizar: '))
    for i in range(tiradas):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        dado3 = random.randint(1, 6)
        suma = dado1 + dado2 + dado3
        print(f'{dado1} + {dado2} + {dado3} = {suma}')

elif opcion == 5:

        def generar_pregunta():
            operadores = ['+', '-', '*', '/']
            op = random.choice(operadores)
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            if op == '/':
                num1 = num1 * num2
            pregunta = f'{num1} {op} {num2}'
            respuesta_correcta = eval(pregunta)
            return pregunta, respuesta_correcta
        def realizar_examen():
            puntaje = 0
            total_preguntas = 15
            for i in range(total_preguntas):
                pregunta, respuesta_correcta = generar_pregunta()
                print(f'Pregunta {i + 1}: {pregunta} = ?')
                respuesta_usuario = float(input('Tu respuesta: '))
                if respuesta_usuario == respuesta_correcta:
                    print('Correcto')
                    puntaje += 1
                else:
                    print(f'Incorrecto. La respuesta correcta era {respuesta_correcta}')
            print(f'Terminaste, tienes {puntaje} puntos de {total_preguntas} respuestas correctas.')
        realizar_examen()