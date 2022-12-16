# Maior número
def maior(x,y,z):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z

    return max

def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro numero: '))

    print("Maior: ", maior(x,y,z))
    print()
    
while True:
    menu()