def comptar_majuscules(cadena):
    comptador = 0
    for lletra in cadena:
        if lletra.isupper():
            comptador = comptador + 1
    return comptador


print(comptar_majuscules("Hola Món"))
print(comptar_majuscules("BON DIA"))
print(comptar_majuscules("python"))
print(comptar_majuscules("Hola Adrian"))
