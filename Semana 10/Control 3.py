import numpy

matriz = numpy.random.rand(5, 5)
matrizriego = numpy.zeros((5, 5))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] < 0.7:
            matrizriego[i][j] = 1

print (matriz)
print (matrizriego)