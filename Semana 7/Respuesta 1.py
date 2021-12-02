#Matías Rodríguez

salida = 0
promediofinal = 0
ponderacionacumulada = 0
while salida == 0:
    nota = input("Ingrese nota (escriba salir o Salir para terminar) ")
    if str(nota) == "salir" or str(nota) == "Salir":
        break
    ponderacion = int(input("Ingrese ponderacion (entre 1-100) de la nota: "))
    ponderacionacumulada += ponderacion
    if float(nota) < 1 or float(nota) > 7:
        salida = 1
        if float(nota) < 1:
            print("La nota debe ser mayor o igual a 1 - ERROR!")
        else:
            print("La nota debe ser menor o igual a 7 - ERROR!")
    elif ponderacion < 1 or ponderacion > 100 or ponderacionacumulada > 100:
        salida = 1
        if ponderacion < 1:
            print("La ponderacion debe ser mayor o igual a 1 - ERROR!")
        else:
            print("La ponderacion debe ser menor o igual a 100 - ERROR!")
    promediofinal += float(nota) * (ponderacion/100)
print("El promedio final es:")
print(promediofinal)