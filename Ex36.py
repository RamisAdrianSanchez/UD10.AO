def es_de_traspas(any):
    if any % 400 == 0:
        return True
    elif any % 100 == 0:
        return False
    elif any % 4 == 0:
        return True
    else:
        return False

any = int(input("Introdueix un any: "))

if es_de_traspas(any):
    print("L'any és de traspàs")
else:
    print("L'any no és de traspàs")