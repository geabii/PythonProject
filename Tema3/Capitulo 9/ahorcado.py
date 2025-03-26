import random

palabras = [
    "noche", "bolso", "cultura", "quedar", "tren", "agotar", "jarabe", "gran", "hombre", "viento",
    "aire", "oportunidad", "ahorrar", "jardín", "divertido", "vida", "cima", "esfuerzo", "coche",
    "hielo", "aprender", "llama", "buscar", "daño", "balance", "pueblo", "familia", "increíble",
    "complejo", "amistad", "cercano", "herida", "fuego", "harina", "bueno", "gritar", "café", "plaza",
    "naranja", "juego", "pan", "tensión", "comida", "hambre", "donde", "drama", "banco", "animal",
    "lago", "irritar", "freno", "corazón", "fiesta", "poder", "enfocar", "gato", "mariposa", "ayer",
    "espejo", "grupo", "marcha", "idea", "duro", "deporte", "gente", "rojo", "raíz", "cabra", "jugar",
    "sueño", "boca", "vista", "carta", "lámpara", "risa", "pelota", "cura", "banco", "cielo", "océano",
    "nieve", "zapatilla", "zebra", "tarde", "aliento", "fama", "salir", "abrazar", "deseo", "adiós",
    "volar", "volver", "borrar", "luz", "libro", "color", "correr", "terreno", "arco", "fuerza"
]



def coger_palabra():
    return random.choice(palabras).lower()


def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)


def dibujo(intentos):
    dibujos = [
        """
           +---+
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          /    |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          / \  |
              ===
        """
    ]
    print(dibujos[6 - intentos])


def jugar():
    palabra = coger_palabra()
    intentos = 6
    letras_adivinadas = set()
    print("\nVamos a jugar al ahorcado")

    while intentos > 0:
        dibujo(intentos)
        print(f"\nPalabra: {mostrar_palabra(palabra, letras_adivinadas)}")
        print(f"Intentos restantes: {intentos}")

        intento = input("Pon una letra o intenta adivinar la palabra completa: ").lower()

        if len(intento) == 1:  # Entrada de una letra
            if intento in letras_adivinadas:
                print("Ya usaste esta palabra.")
            elif intento in palabra:
                letras_adivinadas.add(intento)
                print("Bien. La letra está en la palabra.")
            else:
                intentos = intentos - 1
                print("Incorrecto. La letra no está en la palabra.")
        elif intento == palabra:  # Adivinar la palabra completa
            print("Felicidades. Adivinaste la palabra correctamente.")
            break
        else:
            intentos = intentos - 1
            print("Incorrecto. Esa no es la palabra.")

        if all(letra in letras_adivinadas for letra in palabra):
            print(f"Felicidades Adivinaste la palabra: {palabra}")
            break
    else:
        dibujo(intentos)
        print(f"Perdiste. La palabra era: {palabra}")

    if input("¿Quieres jugar de nuevo? (s/n): ").lower() == "s":
        jugar()
    else:
        print("Gracias por jugar")


if __name__ == "__main__":
    jugar()
