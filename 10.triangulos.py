a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
    
equilatero = a == b == c
isoceles = a == b != c or b == c != a or c == a != b
escaleno = (c < a + b) and (b < a + c) and (a < b + c)

if equilatero:
    print("Triangulo equilatero")
elif isoceles:
    print("Triangulo isoceles")
elif escaleno:
    print("Triangulo Escaleno")
else:
    print("Triangulo invalido")