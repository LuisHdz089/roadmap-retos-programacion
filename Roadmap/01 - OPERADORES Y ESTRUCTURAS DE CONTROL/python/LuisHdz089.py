# Ejemplos de diferentes tipos de operadores en Python
#Operadores Aritméticos
a, b = 10, 3
print("Suma: ", a + b)
print("Resta: ", a - b)
print("Multiplicación: ", a * b)
print("División: ", a / b)
print("División Entera: ", a // b)
print("Módulo: ", a % b)
print("Exponente: ", a ** b)

#Operadores de Comparación
print("Igualdad: ", a == b)
print("Desigualdad: ", a != b)
print("Mayor que: ", a > b)
print("Menor que: ", a < b)
print("Mayor o igual que: ", a >= b)
print("Menor o igual que: ", a <= b)

#Operadores Lógicos
x, y = True, False
print("AND: ", x and y)
print("OR: ", x or y)
print("NOT: ", not x)

#Operadores de Asignación
c = 5
c += 2
print("Asignación y Suma: ", c)
c *= 3
print("Asignación y Multiplicación: ", c)
c -= 4
print("Asignación y Resta: ", c)
c /= 2
print("Asignación y División: ", c)
c %= 3
print("Asignación y Módulo: ", c)
c **= 2
print("Asignación y Exponente: ", c)
c //= 2
print("Asignación y División Entera: ", c)

#Operadores de Identidad
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a
print("list_a es list_b: ", list_a is list_b)
print("list_a es list_c: ", list_a is list_c)
print("list_a no es list_b: ", list_a is not list_b)
print("list_a no es list_c: ", list_a is not list_c)

#Operadores de Pertenencia
frutas = ['apple', 'banana', 'cherry']
print("apple en fruits: ", 'apple' in frutas)
print("grape en fruits: ", 'grape' in frutas)
print("banana no en fruits: ", 'banana' not in frutas)
print("grape no en fruits: ", 'grape' not in frutas)

#Operadores Bit a Bit
m, n = 5, 3  # En binario: 5 = 101, 3 = 011
print("AND Bit a Bit: ", m & n)  # 101 & 011 = 001
print("OR Bit a Bit: ", m | n)   # 101 | 011
print("XOR Bit a Bit: ", m ^ n)  # 101 ^ 011 = 110
print("NOT Bit a Bit: ", ~m)      # ~101 = ...010
print("Desplazamiento a la Izquierda: ", m << 1)  # 101 << 1 = 1010
print("Desplazamiento a la Derecha: ", m >> 1)   # 101 >> 1 = 010

#Operadores de Union en Diccionarios (Python 3.9+)
dict1 = {'a': 1}
dict2 = {'b': 2}
union = dict1 | dict2
print("Unión de Diccionarios: ", union)

#Ejemplo de Estricturas de Control en Python
#Estructura If
nombre = 'Luis'
if nombre == 'Luis':
    print(f"Hola, {nombre}")
#Estructura If-Else
if nombre == 'Ana':
    print(f"Hola, {nombre}")
else:
    print("No eres Ana")

#Estructura If-Elif-Else
if nombre == 'Ana':
    print(f"Hola, {nombre}")
elif nombre == 'Luis':
    print(f"Hola, {nombre}")
else:
    print("No eres Ana ni Luis")

#Estructura for
nombres = ['Ana', 'Luis', 'Carlos']
for n in nombres:
    print(f"Hola, {n}")

for i in range(5):
    print(f"Número: {i}")

for i in range(1,11):
    print(f"Cuadrado de {i} es {i**2}")

for j in range(10,0,-2):
    print(f"Número: {j}")

#Estructura while
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

#Uso de break, continue y pass
for i in range(10):
    if i == 3:
        print("Saltando el 3")
        continue
    if i == 4:
        pass  # No hacer nada
    if i == 5:
        print("Se encontró el 5, saliendo del bucle.")
        break
    print(f"Número: {i}")

#Estructura match-case (Python 3.10+)
comando = "iniciar"
match comando:
    case 'iniciar':
        print("El sistema está iniciando.")
    case 'detener':
        print("El sistema se está deteniendo.")
    case 'reiniciar':
        print("El sistema se está reiniciando.")
    case _:
        print("Comando no reconocido.")

#Estructura try-except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no permitida.")

#Estructura try-except-else-finally
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: División por cero no permitida.") 
else:
    print(f"El resultado es {resultado}")
finally:
    print("Operación finalizada.")

#Ejercicio extra
for i in range(10, 56):
    if i % 2 == 0 and i % 3 != 0 and i != 16:
        print(f"Número que cumple las condiciones: {i}")

contador_inicial = 10
while contador_inicial <= 55:
    if contador_inicial % 2 == 0 and contador_inicial % 3 != 0 and contador_inicial != 16:
        print(f"Número que cumple las condiciones: {contador_inicial}")
    contador_inicial += 1