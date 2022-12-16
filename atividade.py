# Escreva um programa Python para calcular o comprimento de uma cadeia de caracteres. 
def compr_caracter(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(compr_caracter('Daphne é maravilhosa'))