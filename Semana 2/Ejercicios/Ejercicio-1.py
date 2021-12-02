print("A continuación ingrese las notas que sacó durante el semestre")

# Se piden todos los datos necesarios para calcular el promedio del curso
p1 = float(input("Prueba 1: "))
p2 = float(input("Prueba 2: "))
p3 = float(input("Prueba 3: "))

c1 = float(input("Control 1: "))
c2 = float(input("Control 2: "))
c3 = float(input("Control 3: "))
c4 = float(input("Control 4: "))
c5 = float(input("Control 5: "))

t1 = float(input("Tarea 1: "))
t2 = float(input("Tarea 2: "))
t3 = float(input("Tarea 3: "))
t4 = float(input("Tarea 4: "))
t5 = float(input("Tarea 5: "))
t6 = float(input("Tarea 6: "))

p = float(input("Proyecto: "))

# Se calcula el promedio de tareas y Controles
tareas = (t1 + t2 + t3 + t4 + t5 + t6) / 6

controles = (c1 + c2 + c3 + c4 + c5) / 5

# Utilizando el promedio de tareas y controles calculados se procede a calcular la nota final del curso
nf = 0.2*(p1 + p2) + 0.25*p3 + 0.1*tareas + 0.1*p + 0.15*controles

# Se muestra un mensaje que indica la nota final del código insertada en una frase
print(f"Su nota final es {nf}")