import random

numeros = []

maxnumeros = int(input("Ingrese la cantidad de numeros a generar "))
# [minimo, maximo]
minimo = int(input("Ingrese el mínimo numero aleatorio que se puede generar "))
maximo = int(input("Ingrese el máximo numero aleatorio que se puede general "))

for i in range(maxnumeros):
    numero = random.randint(minimo, maximo)
    numeros.append(numero)
print("Lista original")
print(numeros)
# Pares
print("Numeros pares")
for i in range(maxnumeros):
    if numeros[i] % 2 == 0:
        print(numeros[i])    
# Impares
print("Numeros impares")
for i in range(maxnumeros):
    if numeros[i] % 2 != 0:
        print(numeros[i])