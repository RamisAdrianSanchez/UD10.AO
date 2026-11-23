def es_palindrom(paraula):
    if paraula == paraula[::-1]:
        return True
    else:
        return False


print("És un palíndrom?", es_palindrom("radar"))
print("És un palíndrom?", es_palindrom("hola"))
print("És un palíndrom?", es_palindrom("ara"))
print("És un palíndrom?", es_palindrom("civic"))
