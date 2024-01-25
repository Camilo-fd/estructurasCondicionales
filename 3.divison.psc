Algoritmo division
	Escribir "Numero 1:"
	Leer num1
	Escribir "Numero 2:"
	Leer num2
	
	resto = num1 Mod num2
	cociente = num1 / num2
	
	Si resto <> 0 Entonces
		Escribir "La division no exacta"
		Escribir "cociente ", trunc(cociente)
		Escribir "resto ", resto
	SiNo
		Escribir "La division es exacta"
		Escribir "cociente ", trunc(cociente)
		Escribir "resto ", resto
	FinSi
FinAlgoritmo
