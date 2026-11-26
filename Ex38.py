import random


def jugar_mastermind():
    codi_secret = ""

    for i in range(4):
        codi_secret += str(random.randint(0, 9))

    encertat = False

    while not encertat:
        intent = input("Introdueix un codi de 4 xifres: ")

        if len(intent) != 4 or not intent.isdigit():
            print("Has d'introduir exactament 4 xifres.")
            continue

        encerts = 0
        coincideixen = 0

        for i in range(4):
            if intent[i] == codi_secret[i]:
                encerts += 1
            elif intent[i] in codi_secret:
                coincideixen += 1

        print("Nombres en la posició correcta:", encerts)
        print("Nombres que coincideixen però estan en una altra posició:", coincideixen)

        if intent == codi_secret:
            print("Felicitats! Has endevinat el codi!")
            encertat = True

jugar_mastermind()