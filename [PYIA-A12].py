class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")
        
class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")
        

v1 = Veiculo()
v1.movimentar()

v2 = Carro()
v2.movimentar()

v3 = Moto()
v3.movimentar()
