# Autor: José Ignacio Miquel Castro
# Enunciado: Crear un programa en python que cuenta la cantidad de cada una de las vocales que tiene una palabra
'''
Ejemplo

Input: Anestesia

Output:
Cantidad de a: 2
Cantidad de e: 2
Cantidad de i: 1
Cantidad de o: 0
Cantidad de u: 0
'''
# Solicitamos por consola una palabra y la cambiamos a minúsculas
palabra = input("Ingrese una palabra: ").lower()

# Declaramos las variables que guardarán la cantidad de cada una de las vocales. Los nombres de las variables son irrelevantes.
a = 0
e = 0
i = 0
o = 0
u = 0

# Iniciamos un ciclo de tipo for para recorrer el string obtenido anteriormente
for letra in palabra: # Para cada letra del string
  if   letra == "a":  # Comparar la letra con el caracter "a"
    a+=1              # En caso de coincidir, sumar 1 al contador de vocales "a"
  elif letra == "e":  # Comparar la letra con el caracter "e"
    e+=1              # En caso de coincidir, sumar 1 al contador de vocales "e"
  elif letra == "i":  # Comparar la letra con el caracter "i"
    i+=1              # En caso de coincidir, sumar 1 al contador de vocales "i"
  elif letra == "0":  # Comparar la letra con el caracter "o"
    o+=1              # En caso de coincidir, sumar 1 al contador de vocales "o"
  elif letra == "u":  # Comparar la letra con el caracter "u"
    u+=1              # En caso de coincidir, sumar 1 al contador de vocales "u"

# Terminado el ciclo for ya se realizó la cuenta de cada una de las vocales que tiene el string, por lo que procedemos a imprimir por consola los resutlados obtenidos.
print(f"La cantidad de a es: {a}")
print(f"La cantidad de e es: {e}")
print(f"La cantidad de i es: {i}")
print(f"La cantidad de o es: {o}")
print(f"La cantidad de u es: {u}")