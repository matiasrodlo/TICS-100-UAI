#Matías Rodríguez

salida = 0
aciertos = 0
intentos = 0
while salida == 0:
    primervalor = int(input("Cuál es el primer valor a multiplicar? (-1 si desea salir): "))
    if primervalor == -1:
        break
    segundovalor = int(input("Cuál es el segundo valor a multiplicar? (-1 si desea salir): "))
    if segundovalor == -1:
        break
    resultado = primervalor * segundovalor
    respuesta = int(input("Cuantos son " + str(primervalor) + "x" + str(segundovalor) + ": "))
    if respuesta == resultado:
        aciertos += 1
    intentos += 1
print("El porcentaje de aciertos fue de: ", (aciertos / intentos) * 100, "%")