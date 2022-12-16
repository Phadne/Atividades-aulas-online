#  Escreva um programa Python que aceite uma palavra do usuário e reverta-a
word = input("Coloque a frase que será revertida: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")