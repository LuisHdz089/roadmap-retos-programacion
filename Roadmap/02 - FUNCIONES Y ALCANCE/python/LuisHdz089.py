#Funciones basicas en Python
#Funcion sin parametros y sin retorno
def saludar():
    print("Hola, bienvenido a Python!")

saludar()
#Funcion con parametro y sin retorno
def saludar_con_nombre(nombre):
    print(f"Hola, {nombre}, bienvenido a Python!")

saludar_con_nombre("Luis")
#Funcion con parametros y sin retorno
def multiplicar(a, b):
    for i in a:
        print(f"{i} x {b} = {i * b}")

multiplicar([1, 2, 3, 4, 5], 3)
#Funcion con parametros y con retorno
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

area_rectangulo = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {area_rectangulo}")
#Funcion con funcion interna
def calcular_iva(subtotal):
    def iva():
        return subtotal * 0.16
    total = subtotal + iva()
    return total
total_con_iva = calcular_iva(100)
print(f"El total con IVA es: {total_con_iva}")

#Ejemplo de funcion ya cargada en Python
nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}")
help(input)

#Funcion con variable global
contador = 0
def incrementar_contador():
    global contador
    contador += 1
    print(f"Contador: {contador}")
incrementar_contador()
#Funcion con variable local
def funcion_local():
    variable_local = "Soy una variable local"
    print(variable_local)
funcion_local() 
#Funcion con variable global y local
variable_global = "Soy una variable global"
def funcion_mixta():
    variable_local = "Soy una variable local"
    print(variable_local)
    print(variable_global)
funcion_mixta()

#Ejercicio FizzBuzz con funciones
def mi_funcion_fizzbuzz(texto_uno, texto_dos):
    contador_numeros = 0
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto_uno + texto_dos)
        elif i % 3 == 0:
            print(texto_uno)
        elif i % 5 == 0:
            print(texto_dos)
        else:
            print(i)
            contador_numeros += 1
    return contador_numeros

# Ejecución
total = mi_funcion_fizzbuzz("Fizz", "Buzz")
print(f"\n--- Se imprimieron números en lugar de texto {total} veces ---")
