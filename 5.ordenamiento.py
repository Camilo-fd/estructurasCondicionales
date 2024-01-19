cantidad = int(input("Ingrese la cantidad de numeros: \n"))
numero = []
for i in range(cantidad):
    numero.append(input(f"Ingrese el numero: {i + 1}: \n"))

numero_ordenado = sorted(numero) #sorted sirve para ordenar una lista

print(numero_ordenado)