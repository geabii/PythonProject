import re


def calcular_expresion(expresion):
    try:
        # Quitamos los posibles espacios en blanco
        expresion = expresion.replace(" ", "")

        # Expresión regular para ver las posibles multiplicaciones y divisiones, si es así lo mandamos a resolver_mul_div para resolverlo
        """
        Explicación sobre la expresión regular: \d+ coge los número enteros
                                                \.\d+ cogerá un decimal si es que tiene alguno
                                                recogemos el signo, ya sea de multiplicación(*) o de división(/)
        """
        while re.search(r'\d+(\.\d+)?[*/]-?\d+(\.\d+)?', expresion):
            expresion = re.sub(r'(\d+(\.\d+)?)([*/])(-?\d+(\.\d+)?)', resolver_mul_div, expresion)

        # Expresión regular para ver las posibles sumas y restas, si es así lo mandamos a resolver_sum_res para resolverlo
        while re.search(r'\d+(\.\d+)?[+-]-?\d+(\.\d+)?', expresion):
            expresion = re.sub(r'(\d+(\.\d+)?)([+-])(-?\d+(\.\d+)?)', resolver_sum_res, expresion)

        # Convertimos el número final en float
        return float(expresion)
    # Generamos el mensaje de error por si a caso
    except Exception as e:
        return f"Error en la expresión: {e}"

# match representa una parte de la expresión matemática detectada por re.sub
# match group(n) permite acceder a los diferentes grupos cogidos en la expresión regular
# nos saltaremos el 2 y el 5 ya que estos solo cogerían la parte decimal y a nosotros no interesa el número enter que es el 1, el signo que es el 3 y el grupo completo que es el 4
def resolver_mul_div(match):
    num1, op, num2 = float(match.group(1)), match.group(3), float(match.group(4))
    return str(num1 * num2 if op == '*' else num1 / num2)


def resolver_sum_res(match):
    num1, op, num2 = float(match.group(1)), match.group(3), float(match.group(4))
    return str(num1 + num2 if op == '+' else num1 - num2)


if __name__ == "__main__":
    while True:
        expresion = input("Ingrese una operación o 'salir' para terminar: ")
        if expresion.lower() == "salir":
            break
        resultado = calcular_expresion(expresion)
        print("Resultado:", resultado)
