def nums_que_comencen_per(llista, lletra):
    contador = 0

    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            contador += 1

    return contador

noms = ["Adrian", "Maria", "Albert", "Anna", "Joan", "Antonia"]

lletra = input("Introdueix una lletra: ")

print("Noms que comencen per", lletra, ":", nums_que_comencen_per(noms, lletra))
