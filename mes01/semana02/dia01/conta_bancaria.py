from datetime import datetime
import random

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.numero_conta = self.gerar_numero_conta()
        self.historico = [f"Conta criada com saldo inicial: R$ {saldo_inicial:.2f}"]

    def gerar_numero_conta(self):
        return f"{random.randint(10000, 99999)}-{random.randint(1,9)}"

    def adicionar_historico(self, operacao):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.historico.append(f"[{data}] {operacao}")

    def depositar(self, valor):
        if valor <= 0:
            print("Valor deve ser positivo!")
            return
        self.saldo += valor
        self.adicionar_historico(f"Depósito: +R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
        print(f"Depósito realizado! Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor deve ser positivo!")
            return
        if valor > self.saldo:
            print(f"Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}")
            return
        self.saldo -= valor
        self.adicionar_historico(f"Saque: -R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
        print(f"Saque realizado! Novo saldo: R$ {self.saldo:.2f}")

    def transferir(self, conta_destino, valor):
        if valor <= 0:
            print("Valor deve ser positivo!")
            return
        if valor > self.saldo:
            print(f"Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}")
            return
        self.sacar(valor)
        conta_destino.depositar(valor)
        self.adicionar_historico(f"Transferência enviada: R$ {valor:.2f} para {conta_destino.titular}")
        print(f"Transferência realizada para {conta_destino.titular}")

    def extrato(self):
        print("\n Últimas operações:")
        for op in self.historico[-10:]:
            print(op)
        print()



# Banco de dados em memória

contas = {}
conta_logada = None


def criar_conta():
    global contas
    titular = input("Nome do titular: ").strip()
    if titular in contas:
        print("Já existe uma conta com esse titular!")
        return

    saldo_inicial = float(input("Saldo inicial: ") or 0)
    contas[titular] = ContaBancaria(titular, saldo_inicial)
    print(f"Conta criada para {titular}! Número: {contas[titular].numero_conta}")


def login():
    global conta_logada
    titular = input("Digite o nome do titular: ").strip()
    if titular not in contas:
        print("Conta não encontrada!")
        return
    conta_logada = contas[titular]
    print(f"Logado em {conta_logada.titular} ({conta_logada.numero_conta}) | Saldo: R$ {conta_logada.saldo:.2f}")


def menu():
    global conta_logada
    while True:
        print("\n===== BANCO DIGITAL =====")
        if conta_logada:
            print(f"Conta atual: {conta_logada.titular} | Saldo: R$ {conta_logada.saldo:.2f}")
        print("1 - Criar Conta")
        print("2 - Login")
        if conta_logada:
            print("3 - Depositar")
            print("4 - Sacar")
            print("5 - Transferir")
            print("6 - Extrato")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            login()
        elif opcao == "3" and conta_logada:
            valor = float(input("Valor depósito: "))
            conta_logada.depositar(valor)
        elif opcao == "4" and conta_logada:
            valor = float(input("Valor saque: "))
            conta_logada.sacar(valor)
        elif opcao == "5" and conta_logada:
            destino = input("Titular destino: ")
            if destino not in contas:
                print("Conta destino não encontrada!")
                continue
            valor = float(input("Valor transferência: "))
            conta_logada.transferir(contas[destino], valor)
        elif opcao == "6" and conta_logada:
            conta_logada.extrato()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


# Executar o programa
if __name__ == "__main__":
    menu()