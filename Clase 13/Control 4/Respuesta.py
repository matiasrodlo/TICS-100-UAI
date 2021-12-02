archivo = open("Numeros.txt", "r")
pares = []
impares = []
for linea in archivo:
    numero = int(linea)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
archivoPares = open("Pares.txt", "w")
for numero in pares:
    archivoPares.write(str(numero) + "\n")
archivoImpares= open("Impares.txt", "w")
for numero in impares:
    archivoImpares.write(str(numero) + "\n")
archivo.close()
archivoPares.close()
archivoImpares.close()