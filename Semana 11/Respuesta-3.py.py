import random
def cantidadexamenes():
    cantidad  = random.randint(1,50)
    return cantidad

def tiempopcr():
    # 1 significa que el pcr esta en 24 horas, 2 significa que esta en 48 
    tiempo = random.randint(1,2)
    return tiempo

def resultadopcr():
    # 1 significa que el pcr es positivo, 2 significa que es negativo
    resultado = random.randint(1,2)
    return resultado

pcrs = []
positivos = []
negativos = []
positivos24horas = 0
positivos48horas = 0
negativos24horas = 0
negativos48horas = 0
for i in range(7):
    examenesdia = cantidadexamenes()
    pcrs.append(examenesdia)
    positivos.append(positivos24horas)
    negativos.append(negativos24horas)
    positivos24horas = positivos48horas
    positivos48horas = 0
    negativos24horas = negativos48horas
    negativos48horas = 0
    for j in range(examenesdia):
        resultado = resultadopcr()
        tiempo = tiempopcr()
        if resultado == 1:
            if tiempo == 1:
                positivos24horas += 1
            else:
                positivos48horas += 1
        else:
            if tiempo == 1:
                negativos24horas += 1
            else:
                negativos48horas += 1
    
print("Resumen de la semana")
sumapcrs = 0
sumapositivos = 0
sumanegativos = 0
for i in range(7):
    sumapcrs += pcrs[i]
    sumapositivos += positivos[i]
    sumanegativos += negativos[i]
promediopcrs = sumapcrs/7
promediopositivos = sumapositivos/7
promedionegativos = sumanegativos/7
print("Promedio de pcrs por dia", promediopcrs)
print("Promedio de positivos por dia", promediopositivos)
print("Promedio de negativos por dia", promedionegativos)
print("Total de pcrs de la semana", sumapcrs)