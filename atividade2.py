# Escreva um programa Python para somar todos os itens em uma lista
def soma_list(items):
    soma_numeros = 0
    for x in items:
        soma_numeros += x
    return soma_numeros
print(soma_list([90,6,-10]))