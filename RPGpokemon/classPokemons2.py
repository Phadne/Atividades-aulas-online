import random

nomesEletrico = ("Pikachu", "Electabuzz", "Pichu")
nomesAquatico = ("Squirtle", "Blastoise","Wartotle")
nomesFairy = ("Gardevoir","Clefa","Mimikyu")


class Pokemon:
    def __init__(self, nome="", especie = "", ataque=0, defesa=0, hp=0):

        if (nome == ""):
            self._nome = "Richarlison"
        else:
            self._nome = nome

        self._especie = especie

        if (ataque == 0):
            self._ataque = random.randint(30, 50)
        else:
            self._ataque = ataque

        if (defesa == 0):
            self._defesa = random.randint(20, 30)
        else:
            self._defesa = ataque

        if (hp == 0):
            self._hp = random.randint(50, 100)
        else:
            self._hp = hp

    def criarAtributos(self, ataqueInicio, ataqueFinal, defesaInicio, defesaFinal, hpInicio, hpFinal):
        self._ataque = random.randint(ataqueInicio,ataqueFinal)
        self._defesa = random.randint(defesaInicio,defesaFinal)
        self._hp = random.randint(hpInicio,hpFinal)

class PokemonEletrico(Pokemon):
    def __init__(self, nome="", especie ="", ataque=0, defesa=0, hp=0):
        super().__init__(nome, especie, ataque, defesa, hp)

        if (especie == ""):
            self._especie = nomesEletrico[random.randint(0,len(nomesEletrico)-1)]
        else:
            self._especie = especie

        if (nome == ""):
            self._nome = self._especie
        else:
            self._nome = nome

        

        self._tipo = "Elétrico"
        self._movimento = "Choque do Trovão"

        match self._especie:
            case "Pikachu":
                self.criarAtributos(40,60,10,20,50,80)

            case "Pichu":
                self.criarAtributos(20,30,10,20,30,50)
            case _: 
                print("Usou o super")
        if(ataque !=0):
            self._ataque = ataque
        if(defesa !=0):
            self._defesa = defesa
        if(hp !=0):
            self._hp = hp

class PokemonAquatico(Pokemon):
    def __init__(self, nome="", especie="", ataque=0, defesa=0, hp=0):
        super().__init__(nome, especie, ataque, defesa, hp)

        if (especie == ""):
            self._especie = nomesAquatico[random.randint(0,len(nomesAquatico)-1)]
        else:
            self._especie = especie

        if (nome == ""):
            self._nome = self._especie
        else:
            self._nome = nome

        

        self._tipo = "Aquatico"
        self._movimento = "Jato de Água"

        match self._especie:
            case "Squirtle":
                self.criarAtributos(40,60,10,20,50,80)

            case "Wartotle":
                self.criarAtributos(20,30,10,20,30,50)
            case _: 
                print("Usou o super")
        if(ataque !=0):
            self._ataque = ataque
        if(defesa !=0):
            self._defesa = defesa
        if(hp !=0):
            self._hp = hp

        
class PokemonFairy(Pokemon):
    def __init__(self, nome="", especie="", ataque=0, defesa=0, hp=0):
        super().__init__(nome, especie, ataque, defesa, hp)

        if (especie == ""):
            self._especie = nomesFairy[random.randint(0,len(nomesFairy)-1)]
        else:
            self._especie = especie

        if (nome == ""):
            self._nome = self._especie
        else:
            self._nome = nome

        

        self._tipo = "Fairy"
        self._movimento = "Jato de Purpurina"

        match self._especie:
            case "Gardevoir":
                self.criarAtributos(90,66,10,20,50,80)

            case "Clefa":
                self.criarAtributos(80,70,90,20,30,50)
            case _: 
                print("Usou o super")
        if(ataque !=0):
            self._ataque = ataque
        if(defesa !=0):
            self._defesa = defesa
        if(hp !=0):
            self._hp = hp
                    


if __name__ == "__main__":

    pokemon3 = PokemonEletrico(nome = "Quin", especie="Pikachu", hp=600)
    pokemon4 = PokemonAquatico()
    pokemon5 = PokemonFairy()
    print(vars(pokemon3))
    print(vars(pokemon4))
    print(vars(pokemon5))
