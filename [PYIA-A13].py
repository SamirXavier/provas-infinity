class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self._titular = titular
        self._saldo = saldo
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")
        else:
            print("ERROR: O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor <= 0:
            print("ERROR: O valor do saque deve ser positivo.")
        elif valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} efetuado com sucesso!")
        else:
            print("ERROR: Saldo insuficiente.")
    
    def exibir_saldo(self):
        print(f"Saldo da conta de {self._titular}: R$ {self._saldo:.2f}")



conta1 = ContaBancaria("João", 1000.00)
conta1.exibir_saldo()
conta1.depositar(500.00)
conta1.exibir_saldo()
conta1.sacar(200.00)
conta1.exibir_saldo()
conta1.sacar(1500.00)
conta1.exibir_saldo()
