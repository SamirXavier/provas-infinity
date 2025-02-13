class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def falar(self):
        print("esse animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome}: O cachorro late.")

class Gato(Animal):
    def falar(self):
        print(f"{self.nome}: O gato mia.")
        

rex = Cachorro('Rex')
dan = Gato('Danone')

rex.falar()
dan.falar()