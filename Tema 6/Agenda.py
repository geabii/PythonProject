contactos={}

def menu():
    while True:
        print("1. Añadir contacto")
        print("2. Mostrar contactos")
        print("3. Eliminar contactos")
        print("4. Editar contactos")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del contacto: ")
            if nombre in contactos:
                print("El contacto ya existe, si se equivocó deje \"Primer apellido\" vacío para para de añadir ese contacto.")
            apellido1 = input("Introduce el primer apellido del contacto: ")
            if apellido1 == "":
                continue
            apellido2 = input("Introduce el segundo apellido del contacto: ")
            telefono = int(input("Introduce el número del contacto: "))
            if telefono > 999999999:
                print ("El número De teléfono es demasiado largo., debe contener 9 cifras")
                print("Aún así si el número introducido es el que deseas mantener déjelo como está, sin embargo si se equivocó de verdad deberá eliminar el contacto e introducir correctamente el número ")
            elif telefono < 100000000:
                print("El número de teléfono es demasiado pequeño, debe contener 9 cifras")
                print("Aún así si el número introducido es el que deseas mantener déjelo como está, sin embargo si se equivocó de verdad deberá eliminar el contacto e introducir correctamente el número ")

            contacto = {"Nombre": nombre, "Primer apellido": apellido1, "Segundo apellido": apellido2, "Teléfono": telefono}
            contactos[nombre] = contacto
        elif opcion == "2":
            if not contactos:
                print("La agenda no tiene contactos.")
            else:
                for nombre, contacto in contactos.items():
                    print(f"Nombre: {nombre}")
                    print(f"Primer Apellido: {contacto['Primer apellido']}")
                    print(f"Segundo Apellido: {contacto['Segundo apellido']}")
                    print(f"Teléfono: {contacto['Teléfono']}")
                    print("-" * 20)
        elif opcion == "3":
            eliminar = input("Nombre del contacto que desea eliminar: ")
            if eliminar in contactos:
                contactos.pop(eliminar)
                print("El contacto ha sido eliminado.")
            else:
                print("El contacto no existe")
        elif opcion == "4":
                nombre = input("Nombre del contacto que desea eliminar: ")
                if nombre not in contactos:
                    print('El contacto no existe.')
                    continue

                print("¿Qué campo quieres modificar?"
                      "\n1. Nombre"
                      "\n2. Primer apellido"
                      "\n3. Segundo apellido"
                      "\n4. Teléfono")
                campo = input("Selecciona el campo que quieres modificar: ")
                if campo == "1":
                    nuevo_nombre = input("Introduce el nuevo nombre: ")
                    contactos[nuevo_nombre] = contactos.pop(nombre)
                    contactos[nuevo_nombre]['Nombre'] = nuevo_nombre
                    print("Nombre actualizado correctamente.")
                elif campo == "2":
                    nuevo = input("Introduce el nuevo primer apellido: ")
                    contactos[nombre]['Primer apellido'] = nuevo
                    print("Primer apellido actualizado.")
                elif campo == "3":
                    nuevo = input("Introduce el nuevo segundo apellido: ")
                    contactos[nombre]['Segundo apellido'] = nuevo
                    print("Segundo apellido actualizado.")
                elif campo == "4":
                    while True:
                        nuevo_tel = input("Introduce el nuevo teléfono debe contener 9 cifras: ")
                        if nuevo_tel.isdigit() and len(nuevo_tel) == 9:
                            contactos[nombre]['Teléfono'] = int(nuevo_tel)
                            print("Teléfono actualizado.")
                            break
                        else:
                            print("Número no válido, debe contener exactamente 9 cifras.")
                else:
                    print("Opción no válida. Intenta de nuevo.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")


menu()