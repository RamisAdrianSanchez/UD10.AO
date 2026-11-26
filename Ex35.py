def comptar_vocals(paraula):
    vocals = "aeiou"

    for vocal in vocals:
        contador = paraula.lower().count(vocal)
        print(vocal, ":", contador)

paraula = input("Introdueix una paraula: ")
comptar_vocals(paraula)