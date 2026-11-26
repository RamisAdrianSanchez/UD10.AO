def filtrar_paraules(llista, x):
    resultat = []
    for paraula in llista:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat

paraules = ["casa", "ordinador", "sol", "teclat", "ratoli"]
x = 4

print(filtrar_paraules(paraules, x))
