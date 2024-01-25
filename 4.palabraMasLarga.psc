Algoritmo sin_titulo
	Escribir "Ingrese la primera palabra: " 
    Leer palabra1
    Escribir "Ingrese la segunda palabra: "
    Leer palabra2
	
    longitud_palabra1 = Longitud(palabra1)
    longitud_palabra2 = Longitud(palabra2)

    Si longitud_palabra1 > longitud_palabra2 Entonces
        Escribir palabra1, " es más larga que ", palabra2
    Sino
        Si longitud_palabra2 > longitud_palabra1 Entonces
            Escribir palabra2, " es más larga que ", palabra1
        Sino
            Escribir("Ambas palabras tienen la misma longitud.")
        FinSi
    FinSi
FinAlgoritmo
