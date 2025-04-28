import random

def crear_tablero(columnas, filas, numero_minas):
    # Para cada casilla del juego colocamos un espacio en blanco
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    minas = set()
    # Mientras que las minas del tablero sean menores a todas las que debería haber (20), haremos lo siguiente
    while len(minas) < numero_minas:
        # Ponemos posición aleatoria de fila y columna, le estamos indicando que coja un número aleatorio entre 0 y filas -1
        # (como más tarde le indicaremos que filas es igual a 10 en este caso con -1 le diremos que es hasta el 9)
        fila = random.randint(0, filas - 1)
        colum = random.randint(0, columnas - 1)
        if (fila, colum) not in minas:
            minas.add((fila, colum))
    return tablero, minas

def contar_minas_alrededor(fila, colum, minas, filas, columnas):
    direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    contar = 0
    for df, dc in direcciones:
        nf, nc = fila + df, colum + dc
        if 0 <= nf < filas and 0 <= nc < columnas and (nf, nc) in minas:
            contar += 1
    return contar


def descubrir(tablero, fila, colum, minas, filas, columnas, descubiertas):
    if (fila, colum) in descubiertas or tablero[fila][colum] != ' ':
        return
    descubiertas.add((fila, colum))
    if (fila, colum) in minas:
        tablero[fila][colum] = 'X'
        return
    num_minas = contar_minas_alrededor(fila, colum, minas, filas, columnas)
    tablero[fila][colum] = str(num_minas) if num_minas > 0 else '.'
    if num_minas == 0:
        for df, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nf, nc = fila + df, colum + dc
            if 0 <= nf < filas and 0 <= nc < columnas:
                descubrir(tablero, nf, nc, minas, filas, columnas, descubiertas)


def imprimir_tablero(tablero):
    print("   " + " ".join(str(i) for i in range(len(tablero[0]))))
    print("  " + "-" * (len(tablero[0]) * 2))
    for i, fila in enumerate(tablero):
        print(f"{i} |" + " ".join(fila))






def jugar():
    filas, columnas, numero_minas = 10, 10, 20
    tablero, minas = crear_tablero(filas, columnas, numero_minas)
    descubiertas = set()

    while True:
        imprimir_tablero(tablero)
        try:
            fila = int(input("Ingrese número de fila: "))
            colum = int(input("Ingrese número de columna: "))
            if (fila, colum) in minas:
                print("Acabas de explotar.")
                break
            descubrir(tablero, fila, colum, minas, filas, columnas, descubiertas)
        except ValueError:
            print("Coordenadas incorrectas, vuelve a introducir coordenadas.")
        if len(descubiertas) + len(minas) == filas * columnas:
            print("Enhorabuena, has ganado sin explotar.")
            break


jugar()