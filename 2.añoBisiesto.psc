Algoritmo añoBisiesto
	Escribir "Ingrese el año"
	Leer ano
	
	Si ano <= 1599 Entonces
		Si (ano MOD 4 == 0) Entonces
			Escribir ano, " es bisiesto"
		SiNo
			Escribir ano, " no es bisiesto"
		FinSi
	SiNo
		Si (ano MOD 100 == 0 y ano MOD 400 == 0) Entonces
			Escribir ano " es bisiesto"
		SiNo
			Si (ano MOD 4 == 0) Entonces
				Si (ano MOD 100 <> 0) Entonces
					Escribir ano, " es bisiesto"
				SiNo
					Escribir ano, " no es bisiesto"
				FinSi
			SiNo
				Escribir ano, " no es bisiesto"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
