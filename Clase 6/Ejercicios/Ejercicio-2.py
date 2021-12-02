# Autor: José Ignacio Miquel Castro
# Enunciado: Escribir un programa en python que solicite al usuario ingresar una palabra y hacer que el programa retorne si esta palabra es un palíndrome o no lo es

# Se solicita una palabra por consola
palabra = input("Ingrese una palabra: ").lower() # el ".lower()" pasa todas las letras a minúsculas para evitar problemas

# Creamos una variable que indica cuantas diferencias encontramos entre las letras que se compararán. De esta forma si el número sigue siendo 0 quiere decir que la palabra ingresada es un palíndrome
diferencias = 0

# Creamos un ciclo de tipo for para recorrer las letras de la palabra y compararlas con la letra que corresponde
for i in range(0,len(palabra)):

  # Si las letras son diferentes se suma 1 al contador de diferencias. Cabe destacar que si esto sucede, la palabra ingresada no es un palíndrome por lo que se puede poner un break dentro del condicional.
  if palabra[i] != palabra[len(palabra) - 1 - i]:
    diferencias+=1
    # break

# En caso de que haya 0 diferencias se imprime por consola que la palabra ingresada es un palíndrome
if diferencias == 0:
  print("La palabra ingresada es un palíndrome.")

# En caso contrario, se imprime por consola que la palabra ingresada no es un palíndrome
else:
  print("Lapalabra ingresda NO  es un palíndrome.")