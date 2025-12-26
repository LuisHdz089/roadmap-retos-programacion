#Estructuras de Datos en Python
#Listas
#Creación de una lista
lenguajes = ["Python", "Java", "C++", "JavaScript"]
print("Lista de lenguajes:", lenguajes)
#Insertar un elemento
lenguajes.append("Ruby")
print("Lista de lenguajes:", lenguajes)
#Eliminar un elemento
lenguajes.remove("C++")
print("Lista de lenguajes:", lenguajes)
#Acceder a un elemento
primer_lenguaje = lenguajes[0]
print("Primer lenguaje:", primer_lenguaje)
#Actualizar un elemento
lenguajes[1] = "Java 11"
print("Lista de lenguajes actualizada:", lenguajes)
#Ordnenar la lista
lenguajes.sort()
print("Lista de lenguajes ordenada:", lenguajes)

#Tuplas
#Creación de una tupla
coordenadas = (10.0, 20.0)
#Acceder a un elemento
x = coordenadas[0]
y = coordenadas[1]
print("Coordenadas:", x, y)
#Las tuplas son inmutables, no se pueden modificar
#Ordenar una tupla (creando una nueva)
tupla_ordenada = sorted(coordenadas)
print("Tupla ordenada:", tupla_ordenada)

#Diccionarios
#Creación de un diccionario
persona = {"nombre": "Luis", "edad": 30, "ciudad": "Madrid"}
#Insertar un elemento
persona["profesion"] = "Ingeniero"
#Eliminar un elemento
del persona["ciudad"]
#Acceder a un elemento
nombre = persona["nombre"]
print("Nombre:", nombre)
#Actualizar un elemento
persona["edad"] = 31
print("Diccionario de persona actualizado:", persona)
#Ordenar un diccionario por claves
persona_ordenada = dict(sorted(persona.items()))
print("Diccionario de persona ordenado por claves:", persona_ordenada)

#Conjuntos
#Creación de un conjunto
numeros = {1, 2, 3, 4, 5}
#Insertar un elemento
numeros.add(6)
#Eliminar un elemento
numeros.remove(3)
#Acceder a elementos (no se puede acceder por índice)
print("Conjunto de números:", numeros)
#Actualizar un conjunto (agregar varios elementos)
numeros.update({7, 8, 9})
#Ordenar un conjunto (creando una lista ordenada)
numeros_ordenados = sorted(numeros)


agenda = {}
def agregar_contacto():
    print("Ingrese un ID para el Contacto:")
    id = int(input())
    print("Ingrese el nombre de su contacto:")
    nombre = input()
    print("Ingrese el número de teléfono de su contacto:")
    telefono = input()
    if len(telefono) == 10:
        agenda[id] = {'nombre': nombre, 'telefono': telefono}
        print("Contacto agregado exitosamente.")
    else:
        print("El número de teléfono debe tener 10 dígitos.")

def buscar_contacto():
    print("Ingrese el ID del contacto a buscar:")
    id = int(input())
    if id in agenda:
        contacto = agenda[id]
        print(f"ID: {id}, Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
    else:
        print("Contacto no encontrado.")

def actualizar_contacto():
    print("Ingrese el ID del contacto a actualizar:")
    id = int(input())
    print("Cambiara Nombre, Teléfono o ambos? (n/t/a)")
    opcion = input().lower()
    if id in agenda:
        contacto = agenda[id]
        if opcion == "n":
            print("Ingrese el nuevo nombre:")
            contacto['nombre'] = input()
        elif opcion == "t":
            print("Ingrese el nuevo teléfono:")
            telefono = input()
            if len(telefono) == 10:
                contacto['telefono'] = telefono
                print("Teléfono actualizado exitosamente.")
            else:
                print("El número de teléfono debe tener 10 dígitos.")
        elif opcion == "a":
            print("Ingrese el nuevo nombre:")
            contacto['nombre'] = input()
            print("Ingrese el nuevo teléfono:")
            telefono = input()
            if len(telefono) == 10:
                contacto['telefono'] = telefono
                print("Contacto actualizado exitosamente.")
            else:
                print("El número de teléfono debe tener 10 dígitos.")
        else:
            print("Opción no válida.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    print("Ingrese el ID del contacto a eliminar:")
    id = int(input())
    if id in agenda:
        del agenda[id]
        print("Contacto eliminado exitosamente.")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos():
    if agenda:
        for id, contacto in agenda.items():
            print(f"ID: {id}, Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
    else:
        print("No hay contactos en la agenda.")

def menu():
    while True:
        print("\n----- Menú de la Agenda -----")
        print("1. Agregar | 2. Buscar | 3. Actualizar | 4. Eliminar | 5. Todos | 6. Salir")
        
        comando = input("Ingrese una opción: ")

        match comando:
            case "1": agregar_contacto()
            case "2": buscar_contacto()
            case "3": actualizar_contacto()
            case "4": eliminar_contacto()
            case "5": mostrar_contactos()
            case "6":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida.")

menu()

