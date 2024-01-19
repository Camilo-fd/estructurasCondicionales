from time import localtime
t = localtime()
año = int(input("Año: "))
mes = int(input("Mes: "))
dia = int(input("Dia: "))
año_actual = t.tm_year
mes_actual = t.tm_mon
dia_actual = t.tm_mday
edad = año_actual - año
if(dia_actual < dia and mes_actual <= mes):
    edad -= 1
print(edad)