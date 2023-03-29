class Pessoa:
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João",20)
print(p1.nome)