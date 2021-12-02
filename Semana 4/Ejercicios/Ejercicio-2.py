# Programa que solicita al usuario ingresar un número para luego indicar si este es primo o no lo es

# Pedimos al usuario que ingrese el número a evaluar
n = int(input("Ingrese un número mayor que 0: "))

# Se declara una variable para contar la cantidad de divisores que tiene el número
contador_divisores = 0

# Se crea una nueva variable que guardará el valor original ingresado por el usuario
num = n

# Creamos un ciclo while para probar si la división tiene resto para cada número entre el 1 y el número entregado por el usuario
while (n > 0):

  # Se pregunta si la división es exacta
  if (num%n == 0):

    # Si la división es exacta se suma 1 al contador de divisores
    contador_divisores += 1

  # Se resta 1 al contador n para probar el siguiente número a evaluar
  n = n - 1

# Se evalua la cantidad de divisores y se imprime la respuesta en cada caso
if contador_divisores==2:
  print(f"{n} es un numero primo.")
elif n==1:
  print(f"{n} es un numero primo")
else:
  print(f"{n} no es un numero primo")