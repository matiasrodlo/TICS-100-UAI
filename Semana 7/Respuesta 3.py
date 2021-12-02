#Matías Rodríguez

e = 0
cantidaditeraciones = int(input("Ingrese la cantidad de iteraciones: "))
contador = 0
while contador < cantidaditeraciones:
    e += 1/((contador + 1) ** 2)
    contador += 1
valorpi = (6 * e) ** 0.5
print("PI calculado con ", cantidaditeraciones, " iteraciones es:", valorpi)