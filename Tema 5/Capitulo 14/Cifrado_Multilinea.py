tamano_max = 27

def obtenerModo():
    while True:
        print('quieres encriptar o desencriptar')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d'.split():
            return modo
        else:
            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')

def obtenerMensaje():
    if modo[0] == 'e':
        print('Ingresa tu mensaje (solo se podrán introducir letras):')
        return input().lower()
    else:
        print('Ingresa tu mensaje (números separados por espacios):')
        entrada = input()
        return [int(n) for n in entrada.split() if n.isdigit()]

def obtenerClave():
    while True:
        print(f'Ingresa e número de clave(1-{tamano_max}): ')
        clave = int(input())
        if 1 <= clave <= tamano_max:
            return clave

def letra_numero(letra):
    return ord(letra) - ord('a') + 1

def numero_letra(numero):
    numero = (numero - 1)% 26 + 1
    return chr(ord('a') + numero - 1 )

def obtenerMensajeTraducido(modo, mensaje, clave):
    resultado=''
    if modo[0] == 'e':
        resultado_numeros = []
        for letra in mensaje:
            if letra.isalpha():
                num = letra_numero(letra)
                num += clave
                resultado_numeros.append(str((num - 1) % 26 + 1))
        return ' '.join(resultado_numeros)
    else:
        for num in mensaje:
            num -= clave
            resultado += numero_letra(num)
        return resultado


modo = obtenerModo()
mensaje = obtenerMensaje()
clave = obtenerClave()

print('Tu texto traducido es:')
print(obtenerMensajeTraducido(modo,mensaje,clave))