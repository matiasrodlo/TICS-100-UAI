# Crée un código que lea el archivo "notas.txt", guarde su información en una matríz (hecha con listas) y luego agregue el promedio
# de notas a cada uno de los alumnos dentro de la matríz. Finalmente, imprima la matríz con los promedios incluidos.

with open("notas.txt", "r") as archivo:
    lineas = archivo.readlines()
    libro = []
    for linea in range(len(lineas)):
        libro.append(lineas[linea].split(","))
        for elemento in range(len(libro[linea])):
            libro[linea][elemento] = libro[linea][elemento].replace("\n", "")
for linea in range(1,len(libro)):
    promedio = 0
    for nota in range(2,len(libro[linea])):
        promedio += float(nota)
    promedio = promedio / (len(libro[linea]) - 2)
    libro[linea].append(promedio)

libro[0].append("PROM")
for linea in libro:
    print(linea)

with open("notas.txt", "w") as archivo:
    lineas_nuevas = []
    for fila in libro:
        elemento = ""
        for var in range(len(fila)-1):
            elemento= elemento+fila[var]+","
        elemento = elemento+str(fila[len(fila)-1])+"\n"
        lineas_nuevas.append(elemento)
    archivo.writelines(lineas_nuevas)