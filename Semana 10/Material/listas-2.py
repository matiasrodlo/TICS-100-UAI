import numpy

a = numpy.array([1, 2, 3])

a.size

lista = [3,5,4,7,6,2,4]

max = lista[0]

for i in range(0,len(lista)):
    if(lista[i]>max):
        max = lista[i]

print(f"El máximo es: {max}")