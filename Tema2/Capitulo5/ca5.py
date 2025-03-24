# Pedir la lista de los integrantes
integrantes = []
while True:
    integrante = input("Introduce el nombre del integrante, si ya no quedan más déjelo en blanco : ")
    if integrante == "":
        break
    integrantes.append(integrante)
# Hacemos la cadena de texto
salida = "/#################################\\ \n\n"
salida += "- Integrantes:\n\n"
for integrante in integrantes:
    salida += f"\t- {integrante}\n\n"

salida += "/#################################\\"

# Imprimir la lista formateada
print(salida)

