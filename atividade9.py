# Escreva um programa Python para a soma de dois inteiros dados. No entanto, se a soma estiver entre 15 a 20, ela retornará 20.
def soma(x, y):
    soma = x + y
    if soma in range(15, 20):
        return 20
    else:
        return soma

print(soma(20, 6))
print(soma(17, 2))
print(soma(19, 12))