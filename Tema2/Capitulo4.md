# Capítulo 4

## Adivina el número

* Programa
* ![Ejemplos](imagenes_capitulo_4/adivina.png)
* Código
![Ejemplos](imagenes_capitulo_4/codigo.png)
* Explicación del código línea a línea
  * 1 Importamos un número aleatorio
  * 2 Inicializamos la variable "intentosRealizados" a 0
  * 3 Sacamos por pantalla un mensaje de bienvenida y preguntamos nombre del usuario
  * 4 Ponemos un input() para que el usuario introduzca su nombre
  * 5 Indicamos que el número será un número random entero(int) entre el 1 y el 20
  * 6 Sacamos por pantalla un mensaje para dar a entender al usuario que va a empezar el juego
  * 7 Comenzamos el bucle(while), indicando que si los intentos realizados son menores a 6 seguirá el juego
  * 8 Empezamos a escribir dentro el bucle sacando por pantalla un mensaje
  * 9 Le pedimos un número al usuario para que guarde en la variable "estimación"
  * 10 Le indicamos que estimación tiene que ser un número entero
  * 11 Al escribir un número sumaremos 1 al número de intentos realizados
  * 12 Si el número introducido es menor al número generado
  * 13 Le indicaremos al usuario que su número es menor al resultado
  * 14 Si el número introducido es mayor al número generado
  * 15 Le indicaremos al usuario que su número es mayor al resultado
  * 16 El número es igual que el resultado
  * 17 Paramos el bucle
  * 18 Si el número es igual que el resultado
  * 19 Meteremos en una cadena(string(str)) el número de intentos realizados por el usuario
  * 20 Mensaje por pantalla que le dará a entender al usuario que ha ganado el juego indicándole cuantos intentos a tenido
  * 21 Si el número no es igual(!=) al resultado después de los 6 intentos
  * 22 Meteremos el resultado en una cadena
  * 23 Sacaremos por pantalla un mensaje que le indique al usuario que no ha ganado y le diremos cual era el resultado