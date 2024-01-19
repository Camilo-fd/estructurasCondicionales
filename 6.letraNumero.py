caracter = input("Ingrese el caracter: ")

if caracter.isalpha():
    if caracter.isupper(): #isupper() determina si es mayuscula
        print(f"{caracter} es una mayuscula")
    elif caracter.islower(): #islower() determina si es minuscula
        print(f"{caracter} es una minuscula")
else:
    if caracter.isdigit(): #isdigit() determina si es digito
        print(f"{caracter} es un digito")
    else:
        print("No es letra ni numero")