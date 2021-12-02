# Programa que determina si una fecha ocurre antes o después que otra. Se ingresa día, mes y año de ambas fechas a comparar.

# Pedimos los datos de las fechas a comparar
# Fecha 1
dia1 = int(input("Ingrese el día de la fecha 1: "))
mes1 = int(input("Ingrese el mes de la fecha 1: "))
year1 = int(input("Ingrese el año de la fecha 1: "))

# Fecha 2
dia2 = int(input("Ingrese el día de la fecha 2: "))
mes2 = int(input("Ingrese el mes de la fecha 2: "))
year2 = int(input("Ingrese el año de la fecha 2: "))

# Comparamos el valor de los años
if(year1 < year2):
    print("La segunda fecha ocurre después que la primera")
elif(year1 > year2):
    print("La primera fecha ocurre después que la segunda")
else: # Si entramos a este else es porque los años son iguales
    #Comparamos los meses de las fechas (dentro del caso en que los años son iguales)
    if(mes1 < mes2):
        print("La segunda fecha ocurre después que la primera")
    elif(mes1 > mes2):
        print("La primera fecha ocurre después que la segunda")
    else: # Si entramos a este else es porque tanto el mes como el año son iguales en ambas fechas
        if(dia1 < dia2):
            print("La segunda fecha ocurre después que la primera")
        elif(dia1 > dia2):
            print("La primera fecha ocurre después que la segunda")
        else:
            print("Las fechas ingresadas son iguales.")
