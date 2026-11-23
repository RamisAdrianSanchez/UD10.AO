def crear_punts(llista):
    for numero in llista:
        print("." * numero)


def dibuixar_imatge():
    crear_punts([2, 4, 6, 8, 6, 4, 2])


dibuixar_imatge()