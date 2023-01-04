class Pokemon:
    def __init__(self, level, nome, hp, ataque):
        self.level = level
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        print("Pokemon criado")
    def atacar(self):
        print("o Pokemon atacou")
    def checarvantagem(self,pokemonInimigo):

        if(pokemonInimigo.tipo == "Fairy"):
            print(f"O pokemon {self.nome} perdeu para o pokemon do tipo{pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Terra"):
            print(f"O pokemon {self.nome} perdeu para o pokemon do tipo{pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Psiquico"):
            print(f"O pokemon {self.nome} perdeu para o pokemon do tipo{pokemonInimigo.tipo}")
        else:
            ("Tipo de pokemon inválido")

class PokemonFairy(Pokemon):
    def __init__(self, level, nome, hp, ataque):
        super().__init__(level, nome, hp, ataque)
        print("Pokemon do tipo fairy criado.")
    def atacar (self):
        print(f"o pokemon {self.nome}usou uma magic para atacar.")

class PokemonTerra(Pokemon):
    def __init__(self, level, nome,hp, ataque):
        super().__init__(level,nome, hp, ataque)
        print("Pokemon do tipo terra criado.")
    def atacar (self):
        print(f"o pokemon {self.nome} usou uma pedra para atacar.")

class PokemonPsiquico(Pokemon):
    def __init__(self, level, nome, hp, ataque):
        super().__init__(level, nome, hp, ataque)
        print("Pokemon do tipo psiquico criado.")
    def atacar (self):
        print(f"o pokemon {self.nome} usou telesinese para atacar.")

pokemon1 = PokemonFairy (47, "Gardevoir", 78, 150)
pokemon2 = PokemonTerra (45,"Nidoking", 89, 145)
pokemon3 = PokemonPsiquico (32,"Psiduck", 90, 134)

pokemon1.atacar ()
pokemon2.atacar ()
pokemon3.atacar ()