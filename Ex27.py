def paraula_mes_llarga(llista):
    mes_llarga = llista[0]

    for paraula in llista:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula

    return mes_llarga


print("La paraula més llarga és:", paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))
print("La paraula més llarga és:", paraula_mes_llarga(["Casa", "Ordinador", "Sol"]))
print("La paraula més llarga és:", paraula_mes_llarga(["Python", "Programació", "Codi"]))