class Cachorro:
    def __init__(self,nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir (self):
            print('Au')

scooby = Cachorro('scooby doo',6,'Dogue Aelmão')

print(scooby.raca)
    