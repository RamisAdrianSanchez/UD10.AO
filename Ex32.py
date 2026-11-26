def mostrar_majors_que(tupla, numero):
    for valor in tupla:
        if valor > numero:
            print(valor)
            
# Programa principal
valors = input("Introdueix nombres enters separats per espais: ")
tupla = tuple(map(int, valors.split()))

mostrar_majors_que(tupla, 18)