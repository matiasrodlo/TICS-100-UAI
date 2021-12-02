# Se piden los valores de la temperatura en farenheit y la velocidad del viento en mph que se muestra en el display
tempF = float(input("Ingrese la temperatura en farenheit que muestra el display: "))
vientoMPH = float(input("Ingrese la velocidad del viento en mph que muestra el display: "))

# Se transforma la temperatura en farenheit a grados celcius
tempC = (tempF - 32) * 5 / 9

# Se transforma la velocidad del viento en mph a metro/segundo
vientoMS = vientoMPH / 2.237

# Se muestra por consola el resultado de ambas transformaciones injertas en una frase
print(f"La temperatura en grados celcius es {tempC} y la velocidad del viento en metros por segundo es {vientoMS}")