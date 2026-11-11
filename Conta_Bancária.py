class Conta:
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.__saldo = saldo
        self.rendimento_ano = None

    def ver_rendimento(self, valor, dias):
        rendimento_diario = (self.rendimento_ano + 1) ** (1/365) - 1
        resultado = valor
        for dia in range(dias):
            resultado *= (rendimento_diario + 1)
        print(f'O rendimento ao ano do seu banco é de {self.rendimento_ano * 100}%. E R${valor:,.2f} em {dias} dias, renderá R${resultado:,.2f}')
        
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):
        print('Você não pode alterar o saldo diretamente.')

    def __str__(self):
        return (
        f'\n----- {self.__class__.__name__.upper()} CONTA {self.id} -----\n'
        f'\nId: {self.id}\n'
        f'Nome: {self.nome}\n'
        f'Saldo: R${self.saldo:,.2f}\n'
        )

    def sacar(self, valor):
        if valor < 0:
            valor = 0
        elif valor > self.saldo:
            valor = self.saldo
        self.__saldo -= valor
        print(f'\nSaque de R${valor:,.2f} autorizado. Saldo atual: R${self.saldo:,.2f}')

    def depositar(self, valor):
        if  valor > 10_000:
            print('Você não pode depositar mais que R$10,000.00')
        else:
            if valor < 0:
                valor = 0
            self.__saldo += valor
            print(f'\nDepósito de R${valor:,.2f} autorizado. Saldo atual: R${self.saldo:,.2f}')

    def transferir(self, valor, conta):
        if valor < 0:
            print('Você não pode transferir R$0,00')
        elif valor > self.__saldo:
            print('Você não pode transferir um valor mais alto que o seu saldo')
        else:
            self.__saldo -= valor
            conta.__saldo += valor
            print(f'Transferência de R${valor:,.2f} autorizada. Saldo atual: {self.saldo:,.2f}')

class Nubank(Conta):
    def __init__(self, id, nome, saldo):
        super().__init__(id, nome, saldo)
        self.rendimento_ano = 0.20
   
class Picpay(Conta):
    def __init__(self, id, nome, saldo):
        super().__init__(id, nome, saldo)
        self.rendimento_ano = 0.15
   
class Itaú(Conta):
    def __init__(self, id, nome, saldo):
        super().__init__(id, nome, saldo)
        self.rendimento_ano = 0.10