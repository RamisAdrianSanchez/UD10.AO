def comprovar_rima(paraula1, paraula2):
    if paraula1[-3:] == paraula2[-3:]:
        print("Les paraules rimen!")
    elif paraula1[-2:] == paraula2[-2:]:
        print("Les paraules rimen una mica.")
    else:
        print("Les paraules no rimen.")

paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

comprovar_rima(paraula1.lower(), paraula2.lower())