#Criação da classe Conta 
class Conta:
    def __init__(self,saldo, titular):
        self.saldo = saldo
        self.titular = titular
    # Metodo que realiza o calculo de depositos realizados
    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        return self.saldo
        
    # Metodo que realiza o calculo de saques realizados
    def sacar(self, saque):
        self.saldo = self.saldo - saque
        return self.saldo
        
    

obj1 = Conta(500, 'joao')

print(obj1.depositar(700))

print(obj1.sacar(250))