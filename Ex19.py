def sumar_llista(llista):
    suma = 0
    for num in llista:
        suma = suma + num
    return suma


def multiplicar_llista(llista):
    multiplicacio = 1
    for num in llista:
        multiplicacio = multiplicacio * num
    return multiplicacio


print("Suma:", sumar_llista([1, 2, 3, 4]))
print("Multiplicació:", multiplicar_llista([1, 2, 3, 4]))

print("Suma:", sumar_llista([5, 10, 15]))
print("Multiplicació:", multiplicar_llista([2, 3, 4]))
