any_actual = int(input("Introdueix l'any actual: "))

persones = []

for i in range(4):
    nom = input("Introdueix el nom: ")
    naixement = int(input("Introdueix l'any de naixement: "))
    edat = any_actual - naixement
    persones.append([nom, naixement, edat])

print()
print("Nom".ljust(15), "Data naixement".ljust(20), "Anys que farà aquest any")
print("-" * 60)

for persona in persones:
    print(persona[0].ljust(15), str(persona[1]).ljust(20), persona[2])