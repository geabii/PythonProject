import random

def sudoku():
    numeros = [1, 2, 3, 4]
    random.shuffle(numeros) 
    
    filas = [
        numeros[0] + numeros[1] + numeros[2] + numeros[3],
        numeros[1] + numeros[2] + numeros[3] + numeros[0],
        numeros[2] + numeros[3] + numeros[0] + numeros[1],
        numeros[3] + numeros[0] + numeros[1] + numeros[2]
    ]
    
    return filas

def imprimir(juego_sudoku):
    for i, fila in enumerate(juego_sudoku):
        print(" ".join(map(str, fila[:2])) + " | " + " ".join(map(str, fila[2:])))
        if i == 1:
            print("---------")

def juego():
    juego_sudoku = sudoku()
    imprimir(juego_sudoku)

juego()
