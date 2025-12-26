#Ejercicio 04 Cadenas de caracteres

cadena = "  Python es Genial  "
print(cadena)
limpia = cadena.strip()
#Acceso y Propiedades

#Obtener logitud de la cadena
longitud = len(limpia)
print(f"La longitud de la cadena es {longitud}")

#Acceso por indice
print("Imprimiendo el primer caracter de la cadena")
print(limpia[0])
print("Imprimiendo el ultimo caracter de la cadena")
print(limpia[-1])

#Slicing (Subcadenas) [incio:fin:paso]
print("Imprimiendo 'Python'")
print(limpia[0:6])
print("Imprimiendo 'genial'")
print(limpia[10:])
print("Invertir la cadena")
print(limpia[::-1])

#Modificación y Transformación

#MAYUSCULAS y minusculas
print("Imprimiendo la cadena en MAYUSCULAS")
print(cadena.upper())
print("Imprimiendo la cadena en minusculas")
print(cadena.lower())
print("Imprimiendo la cadena solo con el primer caracter en MAYUSCULA")
print(cadena.capitalize())
print("Imprimiendo la cadena Con Letras Mayusculas En Cada Palabra")
print(cadena.title())

#Reemplazo
print("Imprimiendo la cadena con 'Java' en vez de 'Python'")
print(cadena.replace("Python", "Java"))

#Eliminacion de espacios (o caracteres)
espacios = "  limpio   "
print("Imprimiendo cadena sin espacios")
print(espacios.strip())

#Composicion y Division

#Concatenacion y Repeticion
saludo = "Hola" + "mundo" + "en" + "Python"
print("Imprimiendo cadena concatenada y repetida")
print(saludo * 3)

#Division (Split) -> Devuelve una lista
csv = "Hola, mundo, en, Python"
print("Imprimiendo la cadena separada por comas y en forma de lista")
print(csv.split(","))

#Union (Join) -> Une una lista en un string
lista = ["P", "y", "t", "h", "o", "n"]
print("Imprimiendo cadena que estaba separada, en una sola cadena")
print("-".join(lista))

#Interpolacion (f-strings - La forma recomendada)
lenguaje = "Python"
print(f"A mi me gusta el lenguaje: {lenguaje}")

#Busqueda y Verificacion
new_cadena = "Aprendiendo sintaxis de Python"
print("Verificacion de Pertenencia")
print("Python" in new_cadena)
print("Verificacion de si inicia con caracter especifico")
print(new_cadena.startswith("A"))
print("Verificacion de si termina con caracter especifico")
print(new_cadena.endswith("n"))
print("Busqueda de un caracter especifico")
print(new_cadena.find("y"))
print("Contador de caracter repetido en la cadena")
print(new_cadena.count("n"))
print("Verificacion de digitos")
print(new_cadena.isdigit())

#Dificultad extra
def analizar_palabras(p1, p2):
    def limpiar_palabras(p: str) -> str:
        return p.lower().replace(" ", "")
    
    def es_palindromo(p):
        palindromo = p == p[::-1]
        if palindromo:
            print("La palabra es un palindromo")
    
    def es_anagrama(p1, p2):
        anagrama = sorted(p1) == sorted(p2)
        if anagrama:
            print("La palabra es un anagrama")
    
    def es_isograma(p):
        isograma= len(p) == len(set(p))
        if isograma:
            print("La palabra es un isograma") 

    w1 = limpiar_palabras(p1)
    w2 = limpiar_palabras(p2)

    print(("-" * 10) + (f" Resultados de {w1} y {w2} ") + ("-" * 10))
    print(("-" * 10) + (f" Resultados de {w1} ") + ("-" * 10))
    es_palindromo(w1)
    es_isograma(w1)
    print(("-" * 10) + (f" Resultados de {w2} ") + ("-" * 10))
    es_palindromo(w2)
    es_isograma(w2)
    print(("-" * 10) + (f" Resultados de Anagrama ") + ("-" * 10))
    es_anagrama(w1,w2)

analizar_palabras("Roma", "Amor")




