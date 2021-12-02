# Escriba  un  código  que permita  al  usuario  ingresar una palabra  por  consola y
# que luego solicite una segunda palabra.  Posteriormente, deberá reescribir el texto
# cambiando todas las coincidencias de la primera palabra ingresada  por  la  segunda.

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese una palabra: ")

archivo = open ("LA ARRUINADORA DE BODAS.txt", "r")
lineas = archivo.readlines()
lineas_cambiadas = []
for linea in lineas:
    lineas_cambiadas.append(linea.replace(palabra1, palabra2))

archivo.close()
archivo = open("LA ARRUINADORA DE BODAS.txt", "w")
archivo.writelines(lineas_cambiadas)
