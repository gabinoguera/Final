import random

#solicitamos al usuario que ingrese un número entero para el tamaño de la matriz
try:
    n = int(input("Ingrese un número entero para el tamaño de la matriz: "))

except ValueError:
    print("Ingrese un número entero válido para el tamaño de la matriz.")

# Crea una matriz vacía para almacenar el valor del usuario
matriz = [[0 for f in range(n)] for c in range(n)]

# Rellenar la matriz con números aleatorios
for f in range(n):
    for c in range(n):
        matriz[f][c] = random.randint(0, 9)

# Imprime la matriz
print("Matriz generada")
for fila in matriz:
    print(fila)

#creamos listas para filas y para columnas

sumas_filas = []
sumas_columnas = []

#recorremos la matriz, inicializamos en 0 el valor de las filas y aumentamos su valor

for f in range(n):
    suma_fila = 0
    for c in range(n):
        suma_fila += matriz[f][c]
    sumas_filas.append(suma_fila)

#recorremos la matriz, inicializamos en 0 el valor de las columnas y aumentamos su valor
for c in range(n):
    suma_columna = 0
    for f in range(n):
        suma_columna += matriz[f][c]
    sumas_columnas.append(suma_columna)

#imprimimos la suma de filas y columnas
print("suma filas:", sumas_filas)
print("suma columnas:", sumas_columnas)
