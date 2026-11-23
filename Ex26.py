def gran_llista(llista):
    gran = llista[0]

    for numero in llista:
        if numero > gran:
            gran = numero

    return gran


print("El nombre més gran és:", gran_llista([3, 4, 2, 3, 10]))
print("El nombre més gran és:", gran_llista([15, 8, 20, 5]))
print("El nombre més gran és:", gran_llista([1, 2, 3, 4]))
