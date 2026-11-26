import random
import time

def intro():
    print("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar.

Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïlla.
Al final de cada camí hi ha un talaiot. En un viuen els gegants bons que ens convidaran
i en l'altre són uns caníbals afamats.""")

def canviTalaiot():
    talaiot = ""

    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueix 1 o 2: ")

    return talaiot

def trobada(canviTalaiot):
    print("T'estàs apropant al talaiot...")
    time.sleep(2)

    print("Està fosc i és tenebrós...")
    time.sleep(2)

    print("Un gran gegant salta davant teu...")
    time.sleep(2)

    gegantamic = random.randint(1, 2)

    if canviTalaiot == str(gegantamic):
        print("Et convida a menjar...")
        return True
    else:
        print("Se't menja d'un mos... ÑAMÑAMÑAM")
        return False

punts = 0
partidaNova = True

while partidaNova:
    intro()

    nTalaiot = canviTalaiot()

    guanya = trobada(nTalaiot)

    if guanya:
        punts += 1
        print("Has guanyat 1 punt!")
        print("Punts acumulats:", punts)
    else:
        partidaNova = False
        print("Has perdut la partida.")
        print("Punts aconseguits:", punts)

print("Fi del joc.")