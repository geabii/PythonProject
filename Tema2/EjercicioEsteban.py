print('Elige una de las siguientes opciones del menú: \n 1 Calcular el Iva de un producto. \n 2 Calcular superficie y perímetro de un círculo. \n 3 Lista de jugadores. \n 4 Solucionar ecuación de segundo grado. \n 5 Calcular perímetro y área de un cuadrado.')
opcion = int(input('Selecciona la opción: '))
if opcion == 1:
    while True:
        try:
            print("\nMenú de opciones:")
            print("1 IVA 21%")
            print("2 IVA 10%")
            print("3 IVA 4%")
            print("4 Salir del programa")

            IVA = int(input("Selecciona una opción: "))

            if IVA == 4:
                break

            if IVA in [1, 2, 3]:
                precio = float(input("Introduce el precio del producto: "))

                if IVA == 1:
                    iva = precio * 0.21
                elif IVA == 2:
                    iva = precio * 0.10
                else:
                    iva = precio * 0.04

                print(f"El IVA es: {iva:.2f} €") # .2f sirve para definir el número de decimales que quieres mostrar

            else:
                print("Opción no válida, intenta de nuevo.")

        except ValueError:
            print("Error: Por favor, introduce un número válido.")
elif opcion == 2:
    radio = float(input('Introduzca el radio del circulo en cm: '))
    area = 3.1416 * (radio * radio)
    perimetro = 2 * 3.1416 * radio
    print(f'El área del círculo sería {area:.2f}cm y el perímetro sería {perimetro:.2f}cm')
elif opcion == 3:
    # Pedir los jugadores para la lista
    jugadores = []
    while True:
        nombre = input("Introduce el nombre del jugador, si ya no quedan más déjalo en blanco: ")
        if nombre == "":
            break

        try:
            altura = float(input("Introduce la altura del jugador en cm: "))

            # Posición del jugador en base de su altura
            if altura <= 160:
                posicion = "Base"
            elif altura > 170:
                posicion = "Pivot"
            else:
                posicion = "Alero"

            # Agregar jugador a la lista
            jugadores.append((nombre, altura, posicion))

        except ValueError:
            print("Por favor, introduce una altura válida en números.")

    # Hacemos la cadena de texto
    salida = "- Lista de jugadores:\n\n"
    for jugador in jugadores:
        salida += f"\t- Nombre: {jugador[0]}\n"
        salida += f"\t  Altura: {jugador[1]} cm\n"
        salida += f"\t  Posición: {jugador[2]}\n\n"

    # Imprimir la lista formateada
    print(salida)

elif opcion == 4:
    a
elif opcion == 5:
    lado = float(input('Introduzca un lado del cuadrado en cm: '))
    peri =  lado * 4
    areaa = lado * lado
    print(f'El perímetro del cuadrado sería {peri:.2f}cm y el area sería {areaa:.2f}cm')
