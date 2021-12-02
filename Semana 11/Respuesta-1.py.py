numeroclientes = int(input("Ingrese cantidad de clientes a evaluar: "))
clientes = []
# Creo un arreglo con datos del cliente [nombre, edad, sueldo, antiguedad]
for i in range(numeroclientes):
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    sueldobase = int(input("Ingrese sueldo base: "))
    antiguedad = int(input("Ingrese años antiguedad cumplidos: "))
    # Lo guardo en clientes
    clientes.append([nombre, edad, sueldobase, antiguedad])
    # Borro cliente para crear otro

for i in range(numeroclientes):
    # Se calcula la condicion financiera
    if clientes[i][3] >= 2 and clientes[i][2] >= 600000 and clientes[i][1] > 25:
        print(clientes[i][0] + " cumple con condiciones de crédito")