# Programa que permite calcular las soluciones de una ecuación cuadrática de la dorma 0 = a*(x**2) + b*x + c

# Primero pedimos los datos necesarios para calcular las raices (a, b y c)
print("ax^2 + bx + c = 0")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Calculamos el discriminante para conocer la naturaleza de las raices de la ecuación (si son 2 diferentes, dos iguales o no son reales)
disc = b**2-4*a*c


print("Las soluciones a la ecuación son:")
# Preguntamos si estamos en el primer caso (raices reales diferentes)
if(disc > 0):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    print(f"x1 = {x1}  x2 = {x2}")

# Preguntamos si estamos en el segundo caso (raices reales iguales / una raíz real)
if(disc == 0):
    x = -b/(2*a)
    print(f"x1 = {x}  x2 = {x}")

# Preguntamos si estamos en el tercer caso (raices complejas diferentes)
if(disc < 0):
    print(f"x1 = {-b/(2*a)} + {(-disc)**0.5/(2*a)}*i")
    x1 = -b/(2*a) + (-disc)**0.5/(2*a)
    print(f"x2 = {-b/(2*a)} - {(-disc)**0.5/(2*a)}*i")