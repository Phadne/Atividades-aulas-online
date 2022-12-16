# Escreva um programa Python para multiplicar todos os itens em uma lista.
# from math import prod

# i = 1
lista = [1,2,3,4,,56,7,]
# while i < 3:
#     lista.append(int(input(f'Insira o {i}º número inteiro: ')))
#     i += 1
    
# print(f'O produto é: {prod(lista)}')
map(lambda x: x * 2, list)