numero1 = int(input("Ingrese el numero: "))
numero2 = int(input("Ingrese el numero: "))

print("1. Suma\n2. Resta\n3. Multiplicacion\n4. Division")
opcion = int(input("Que operacion desea hacer? "))


if opcion == 1:
    print(numero1 + numero2)
elif opcion == 2:
    print(numero1 - numero2)
elif opcion == 3:
    print(numero1 * numero2)
elif opcion == 4:
    print(numero1 / numero2)
else:
    print("no seleccionaste nada")