num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicació:", num1 * num2)

if num2 != 0:
    print("Divisió:", num1 / num2)
    print("Divisió entera:", num1 // num2)
    print("Mòdul:", num1 % num2)
else:
    print("No es pot dividir entre zero.")

print("Potència:", num1 ** num2)

print("\nCANVI DE BASE")

num_base = int(input("Introdueix un nombre enter: "))

print("Binari:", bin(num_base))
print("Octal:", oct(num_base))
print("Decimal:", num_base)
print("Hexadecimal:", hex(num_base))
