def gran_de_tres(num1, num2, num3):
    if num1 >= num2 and num1> num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("El nombre més gran és: ", gran_de_tres(10,5,8))
print("El nombre més gran és: ", gran_de_tres(3,15,9))
print("El nombre més gran és: ", gran_de_tres(20,12,25))
