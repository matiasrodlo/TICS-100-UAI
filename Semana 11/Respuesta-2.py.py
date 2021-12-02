import random
def diasasistencia():
    asistencia = random.randint(0,90)
    return asistencia

alumnos = []
for i in range(30):
    asistenciarandom = diasasistencia()
    alumnos.append(asistenciarandom)

# obtener el alumno con menos asistencia
menor = 91
posicionalumno = 0
for i in range(30):
    if alumnos[i] < menor:
        menor = alumnos[i]
        posicionalumno = i
print("El alumno con menos asistencia es el alumno: ", posicionalumno)

# Obtener el alumno con mas asistencia
mayor = 0
posicionalumno = 0
for i in range(30):
    if alumnos[i] > mayor:
        mayor = alumnos[i]
        posicionalumno = i
print("El alumno con mas asistencia es el alumno: ", posicionalumno)

# Obtener el promedio de asistencia
suma = 0
for i in range(30):
    suma += alumnos[i]

promedio = suma / 30
print("El promedio de asistencia es: ", promedio)