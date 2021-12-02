# Se pide un valor para calcular su raíz cuadrada
a = float(input("Ingrese el valor de la raíz que quiere calcular: "))

# Se pide el valor de la raíz cuadrada del cuadrado más cercano al valor de la variable 'a'
b = float(input("Ingrese el valor de la raíz del cuadrado exacto más cercano a este valor: "))

# Se aproxima el valor de la raíz cuadrada de 'a' utilizando la fórmula mostrada en clases
raiz = (a + b*b) / (2*b)

# Se muestra por consola el resultado de la aproximación insertado en una frase
print(f"El valor aproximado de la raíz cuadrada de {a} es {raiz}")