import random

def pregunta():
    preguntas = [

        ("¿Cuánto es 5 + 7?", 12),
        ("¿Cuántos lados tiene un hexágono?", 6),
        ("¿Cuántos planetas hay en el sistema solar?", 8),
        ("¿Cuántos continentes hay en la Tierra?", 7),
        ("¿Cuántas patas tiene una araña?", 8),
        ("¿Cuántos minutos tiene una hora?", 60),
        ("¿Cuántos segundos tiene un minuto?", 60),
        ("¿Cuánto es 9 * 9?", 81),
        ("¿Cuántos huesos tiene el cuerpo humano adulto?", 206),
        ("¿Cuánto es la raíz cuadrada de 144?", 12),
        ("¿Cuántos días tiene una semana?", 7),
        ("¿Cuántos jugadores tiene un equipo de fútbol en el campo?", 11),

        ("¿Cuál es la capital de Francia?", ["Berlín", "Madrid", "París", "Lisboa"], 2),
        ("¿Quién escribió 'Don Quijote de la Mancha'?", ["Cervantes", "Shakespeare", "Goethe", "Dante"], 0),
        ("¿Cuál es el metal más abundante en la corteza terrestre?", ["Hierro", "Aluminio", "Cobre", "Plata"], 1),
        ("¿Cuál es el océano más grande?", ["Atlántico", "Índico", "Ártico", "Pacífico"], 3),
        ("¿Cuál es el mamífero más grande del mundo?", ["Elefante", "Ballena azul", "Jirafa", "Hipopótamo"], 1),
        ("¿Quién pintó la Mona Lisa?", ["Van Gogh", "Da Vinci", "Picasso", "Rembrandt"], 1),
        ("¿Cuál es el planeta más grande del sistema solar?", ["Tierra", "Marte", "Júpiter", "Saturno"], 2),
        ("¿Cuál es el símbolo químico del oro?", ["Au", "Ag", "Pb", "Fe"], 0),
        ("¿Cuál es la montaña más alta del mundo?", ["Everest", "K2", "Annapurna", "Makalu"], 0),
        ("¿En qué año llegó el hombre a la Luna?", ["1959", "1969", "1979", "1989"], 1),
        ("¿Cuántos colores hay en el arcoíris?", ["5", "6", "7", "8"], 2)
    ]
    return random.choice(preguntas)

def jugar():
    puntaje = 0
    for i in range(5):
        preg = pregunta()
        if isinstance(preg[1], list):
            print(f"Pregunta {i+1}: {preg[0]}")
            for idx, opcion in enumerate(preg[1]):
                print(f"{idx + 1}. {opcion}")
            respuesta = int(input("Elige la opción correcta (1-4): ")) - 1
            if respuesta == preg[2]:
                print("Correcto")
                puntaje += 1
            else:
                print("Incorrecto.")
        else:
            print(f"Pregunta {i+1}: {preg[0]}")
            respuesta = int(input("Tu respuesta: "))
            if respuesta == preg[1]:
                print("Correcto")
                puntaje += 1
            else:
                print("Incorrecto.")
    print(f"Juego terminado. Tu puntaje fue: {puntaje}/5")

jugar()
