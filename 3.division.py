print("------------------------------")
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
resto = num1 % num2
cociente = int(num1 / num2)

if resto != 0:
    print("La division no exacta")
    print(f"cociente: {cociente}")
    print(f"resto: {resto}")
else:
    print("La division es exacta")
    print(f"cociente: {cociente}")
    print(f"resto: {resto}")
print("------------------------------")