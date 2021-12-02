# Escriba un código que le permita al usuario  ingresar  una  palabra
# y retornar la cantidad de veces que se repite dicha palabra dentro
# del archivo "LA ARRUINADORA DE BODAS.txt"

palabra = input("Ingrese una palabra: ")

coincidencias = 0
with open("LA ARRUINADORA DE BODAS.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        indice = 0
        while (linea.find(palabra,indice) != -1):
            coincidencias+=1
            indice = linea.find(palabra,indice) + 1

print(coincidencias)
