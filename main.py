from pokemon import *
from pessoa import *
from pickle import load  


def escolher_pokemon_inicial(treinador):
    print("Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada".format(treinador))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui três 3 escolhas:")
    print("1 - ", pikachu)
    print("2 - ", charmander)
    print("3 - ", squirtle)

    while True:
        escolha = input("Escolha o seu Pokemon: ")

        if escolha == "1":
            treinador.capturar(pikachu)
            break
        elif escolha == "2":
            treinador.capturar(charmander)
            break
        elif escolha == "3":
            treinador.capturar(squirtle)
            break
        else:
            print("Escolha inválida!")

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            treinador = load(arquivo)
            print("Loading feito com sucesso!!!")
            return treinador
    except Exception as error:
        print("Save não encontrado.")


if __name__ == "__main__":
    print("-----------------------------------")
    print("    Bem-vindo ao RPG de Pokemon    ")
    print("-----------------------------------")

    treinador = carregar_jogo()

    if not treinador:      

        nome = input("Olá, qual é o seu nome: ")

        treinador = Treinador(nome)
        print("Olá {}, esse é um mundo habitado por Pokemons.".format(treinador))
        print("Capture o máximo de pokemons que você conseguir e lute com seus amigos")

        if treinador.pokemons:
            print("Já notei que você tem alguns pokemons")
            treinador.listar_pokemons()
        else:
            print("Você não tem nenhum pokemon. Escolha um")
            escolher_pokemon_inicial(treinador)

        print("Pronto, agora você poderá enfrentar seu arqui-inmigo de infância: Glen")
        glen = Inimigo(nome="Glen", pokemons=[PokemonAgua("Squirtle", level=1)])
        treinador.batalhar(glen)

        salvar_jogo(treinador)     

    while True:
        print("-----" * 10)
        print("O que você deseja fazer?")
        print('''1 - Explorar e tentar encontrar pokemons \n2 - Lutar com um inimigo \n3 - Ver pokemons \n0 - Sair do jogo''')
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Fechando o jogo...")
            break
        elif escolha == "1":
            treinador.explorar()
            salvar_jogo(treinador)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            treinador.batalhar(inimigo_aleatorio)
            salvar_jogo(treinador)
        elif escolha == "3":
            treinador.listar_pokemons()
        else:
            print("Opção inválida!!!")