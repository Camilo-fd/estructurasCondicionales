palabra1 = input("Escribe la palabra: ")
palabra2 = input("Escribe la palabra: ")

largopalabra1 = palabra1
largopalabra2 = palabra2

if largopalabra1 > largopalabra2:
    print(f"La palabra {palabra1} es mas larga que la palabra {palabra2}")
else:
    print(f"La palabra {palabra2} es mas larga que la palabra {palabra1}")