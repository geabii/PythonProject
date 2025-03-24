import random


def bola_8():
    respuestas_generales = [
        "Me da a mi que sí.", "Me da a mi que no.", "Puede ser que sí o ...", "Pregúntame más tarde, no me apetece trabajar ahora.",
        "Claro que no.", "Claro que sí.",
        "No estoy seguro.", "Es muy probable."
    ]

    respuestas_especificas = {
        "¿Cómo": ["Con mucho esfuerzo y dedicación.", "A través de la práctica constante.",
                  "No es sencillo, pero posible."],
        "¿Cuando": ["Cuando el destino lo decida.", "En el momento adecuado.", "Quizás más pronto de lo que piensas."]
    }

    while True:
        pregunta = input("Haz una pregunta a la bola 8, si no quiere hacer más preguntas escriba 'salir': ")
        if pregunta == "salir":
            print("Gracias por jugar.")
            break

        for clave, respuestas in respuestas_especificas.items():
            if pregunta.startswith(clave):
                print(random.choice(respuestas))
                break
        else:
            print(random.choice(respuestas_generales))


bola_8()
