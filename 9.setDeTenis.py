jugadora=int(input("Sets ganados del jugador A: \n"))
jugadorb=int(input("Sets ganados del jugador B: \n"))
dif=abs(jugadora-jugadorb)

if (jugadorb==jugadora and jugadorb==7) or (jugadora>7) or (jugadorb>7):
    print("-Resultado invalido-")
elif (jugadora<6 and jugadorb<6) or (jugadorb==jugadora and jugadora==6):
    print("El set aun no acaba")
elif jugadora>jugadorb:
    if jugadora==7:
        if jugadorb==6 or jugadorb==5:
            print("El ganador es el jugador A")
        elif jugadorb<5:
            print("-Resultado invalido-")
    elif dif>1:
        print("El ganador es el jugador A")
    else:
        print("El set todavía aun no acaba")
elif jugadorb>jugadora:
    if jugadorb==7:
        if jugadora==6 or jugadora==5:
            print("El ganador es B")
        elif jugadora<5:
            print("-Resultado invalido-")
    elif dif>1:
        print("El ganador es el jugador B")
    else:
        print("El set todavía aun no acaba")