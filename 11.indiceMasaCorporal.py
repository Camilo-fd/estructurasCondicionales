estatura = float(input("Ingrese la estatura: "))
peso = float(input("Ingrese el peso: "))
edad = float(input("Ingrese la edad: "))

imc = peso / (estatura ** 2)

            
if edad < 45:
    if imc < 22.0:
        print("La condición de riesgo es baja")
    elif imc > 22.0:
        print("La condición de riesgo es medio")
else:
    if imc < 22.0:
        print("La condición de riesgo es medio")
    elif imc > 22.0:
        print("La condición de riesgo es alta")