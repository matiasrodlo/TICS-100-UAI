# Escriba un código que le pida al usuario ingresar 3 números positivos (se asume que el usuario ingresará números positivos)
# Y que diga si se puede construir un triángulo cuyos lados tengan dichas longitudes. Si el triángulo se puede construir, entregar el área de dicho triángulo.

# El primer paso es pedir las longitudes de los lados para guardarlas en variables
a = float(input("Ingrese longitud del lado A: "))
b = float(input("Ingrese longitud del lado B: "))
c = float(input("Ingrese longitud del lado C: "))

# Luego se aplica la condición de que para toda combinación de lados, la suma del primer lado con el segundo debe ser mayor a la longitud del tercer lado
if (a+b > c and a+c > b and b+c > a):
    # Si la condición se cumple se indica por consola que el triangulo se puede construir
    print(f"Es posible construir un triángulo con lados de longitud a={a}, b={b} y c={c}")
    
    # Y se calcula su área utilizando la fórmula entregada en el enunciado
    s = (a+b+c)/2                                                                   # Calculamos y guardamos el semiperímetro para no tener que escribirlo tantas veces
    A = (s*(s-a)*(s-b)*(s-c))**(1/2)                                                # Calculamos el área del triangulo utilizando el semiperímetro y las longitudes de los lados
    print(f"El área del triángulo de lados a={a}, b={b} y c={c} es A={A}")          # Se entrega el área del triángulo
else:
    # En caso de que las longitudes de los lados ingresados no cumplan con la condición expuesta anteriormente, se indica al usuario que no es posible construir un triángulo con los valores ingresados.
    print(f"No es posible construir un triángulo con lados de longitud a={a}, b={b} y c={c}")