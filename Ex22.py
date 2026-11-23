def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False


print("Hi ha elements en comú?", superposicio([1, 2, 3], [4, 5, 3]))
print("Hi ha elements en comú?", superposicio([1, 2, 3], [4, 5, 6]))
print("Hi ha elements en comú?", superposicio(["poma", "pera"], ["pera", "plàtan"]))
