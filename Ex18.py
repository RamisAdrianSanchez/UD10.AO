def es_vocal(caracter):
    if caracter.lower() in "aeiouàèéíïòóúü":
        return True 
    else:
        return False 


print("És una vocal?", es_vocal("a"))
print("És una vocal?", es_vocal("e"))
print("És una vocal?", es_vocal("b"))
print("És una vocal?", es_vocal("O"))
print("És una vocal?", es_vocal("u"))
