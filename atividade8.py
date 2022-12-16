# Escreva um programa Python para encontrar a mediana de três valores.
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))
if a > b:
    if a < c:
        mediana = a
    elif b > c:
        mediana = b
    else:
        mediana = c
else:
    if a > c:
        mediana = a
    elif b < c:
        mediana = b
    else:
        mediana = c

print("A mediana é", mediana)