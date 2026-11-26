capital = float(input("Introdueix la quantitat a sol·licitar (50000€ - 800000€): "))

while capital < 50000 or capital > 800000:
    print("Quantitat incorrecta.")
    capital = float(input("Introdueix una quantitat entre 50000€ i 800000€: "))

interes = float(input("Introdueix l'interès (0.5% - 13%): "))

while interes < 0.5 or interes > 13:
    print("Interès incorrecte.")
    interes = float(input("Introdueix un interès entre 0.5 i 13: "))

anys = int(input("Introdueix el nombre d'anys (3 - 40): "))

while anys < 3 or anys > 40:
    print("Nombre d'anys incorrecte.")
    anys = int(input("Introdueix un nombre d'anys entre 3 i 40: "))

capital_final = capital * (1 + interes / 100) ** anys

print("El capital final serà de:", round(capital_final, 2), "€")