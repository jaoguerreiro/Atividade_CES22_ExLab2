class Action:  #Classe para acoes solicitáveis

    def execute(self):
        pass

class Account:  #Conta do Cliente

    def __init__(self, saldo, extrato):
        self.saldo = saldo
        self.extrato = extrato

#Receiver
class AccountAction(Account): #aqui se define as ações das funções

    def __init__(self, account):
        self.account = account

    def consultar_saldo(self):                                   #retornar saldo
        print("Seu saldo eh: ", self.account.saldo)

    def consultar_extrato(self):                                  #retornar extrato
        print("Seu extrato de operacoes recentes eh: ", self.account.extrato)

    def fazer_transferencia(self, numero_conta, valor):           #subtrair saldo, atualizar extrato e retornar mensagem
        self.account.saldo -= valor
        self.account.extrato = [-valor] + self.account.extrato
        print("Transferencia para conta ", numero_conta, ", no valor de ", valor," realizada.")

class ConsultarSaldo(AccountAction):  #Concrete Command

    def __init__(self, action):
        self.action = action

    def execute(self):
        self.action.consultar_saldo()

class ConsultarExtrato(AccountAction):  #Concrete Command

    def __init__(self, action):
        self.action = action

    def execute(self):
        self.action.consultar_extrato()

class FazerTransferencia(AccountAction):  #Concrete Command

    def __init__(self, action, numero_conta, valor):
        self.action = action
        self.numero_conta = numero_conta
        self.valor = valor

    def execute(self):
        self.action.fazer_transferencia(self.numero_conta, self.valor)

#Invoker
class Command:          #aqui chama a execução das funções, atraves dos Concrete Commands

    def __init__(self):
        pass

    def place_order(self, action):
        self.action = action
        action.execute()


#cliente:
cliente = Account(54.00, [21, -10, 1000])  #saldo e extrato inicial
action = AccountAction(cliente)
saldo = ConsultarSaldo(action)
extrato = ConsultarExtrato(action)
transf = FazerTransferencia(action, 2380749131, 24)

#invoker
bank = Command()

#Sequencia de comandos:
bank.place_order(saldo)
bank.place_order(extrato)
bank.place_order(transf)
bank.place_order(saldo)
bank.place_order(extrato)