import math

x1 = int(input('Introduce el eje x de tu primer punto: '))
y1 = int(input('Introduce el eje y de tu primer punto: '))
x2 = int(input('Introduce el eje x de tu segundo punto: '))
y2 = int(input('Introduce el eje y de tu segundo punto: '))

print('Ahora según los dos puntos que diste vamos a calcular la distancia entre ellos: ')

# La fórmula para saber la distancia entre los dos puntos sería restar los dos puntos x y elevarlo al cuadrado, haremos lo mismo con los puntos y
# Sumaremos los dos resultados y haremos la raíz cuadrada del resultado de esa suma5

eje_x = (x2 - x1)**2
eje_y = (y2 - y1)**2
suma = eje_x + eje_y
distancia_total = math.sqrt(suma)
distancia_redondeada=round(distancia_total, 2)
print(f'La distancia entre los dos punto es {distancia_redondeada} ')
