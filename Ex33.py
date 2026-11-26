def nums_que_comencen_per(llista):
    contador = 0

    for nom in llista:
        if nom.lower().startswith("a"):
            contador += 1

    return contador

noms = ["Adrian", "Maria", "Albert", "Anna", "Joan", "Antonia"]

print("Noms que comencen per a:", nums_que_comencen_per(noms))