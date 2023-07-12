import random

#solicitamos al usuario que ingrese un número entero para el tamaño de la matriz
try:
    n = int(input("Ingrese un número entero para el tamaño de la matriz: "))

except ValueError:
    print("Ingrese un número entero válido para el tamaño de la matriz.")

#creamos una matriz vacía para almacenar el valor del usuario
matriz = []

#creamos un bucle for para recorrer los valores de n y almacenarlos en una lista
for f in range(n):
    fila = []
    for x in range(n):
        fila.append(random.randint(0,9))
        matriz.append(fila)

#imprimir matriz
print("matriz generada")
for fila in matriz:
    print(fila)

#creamos listas para filas y para columnas

sumas_filas = []
sumas_columnas = []

#recorremos la matriz, inicializamos en 0 el valor de las filas y aumentamos su valor

for f in range(len(matriz)):
    suma_fila = 0
    for x in range(len(matriz[f])):
        suma_fila += matriz[f][x]
    sumas_filas.append(suma_fila)

#recorremos la matriz, inicializamos en 0 el valor de las columnas y aumentamos su valor
for i in range(len(matriz[0])):
    suma_columna = 0
    for j in range(len(matriz)):
        suma_columna += matriz[j][i]
    sumas_columnas.append(suma_columna)

#imprimimos la suma de filas y columnas
print("suma filas:", sumas_filas)
print("suma columnas:", sumas_columnas)