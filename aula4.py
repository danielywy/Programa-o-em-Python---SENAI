# Banco - Sistema de Conta
import time
# Banco com clientes
clientes = {
    '1234': {'nome': 'João', 'senha': 'senha123', 'saldo': 1000.0},  
    '5678': {'nome': 'Maria', 'senha': 'senha456', 'saldo': 1500.0}
}

# Função para mostrar o menu
def mostrar_menu():
    print("\n***** SISTEMA DE BANCO *****")
    time.sleep(0.2)
    print("1. Acessar Conta")
    time.sleep(0.2)
    print("2. Ver Extrato")
    time.sleep(0.2)
    print("3. Fazer Depósito")
    time.sleep(0.2)
    print("4. Fazer Saque")
    time.sleep(0.2)
    print("5. Sair do Sistema")
    time.sleep(0.2)
    print("*****************************")

# Função para acessar a conta
def acessar_conta():
    conta = input("Digite o número da sua conta: ")
    time.sleep(0.2)
    if conta in clientes:
        senha = input("Digite sua senha: ")
        time.sleep(0.2)
        if clientes[conta]['senha'] == senha:
            return conta
        else:
            print("Senha incorreta!")
            time.sleep(0.2)
            return None
    else:
        print("Conta não encontrada!")
        time.sleep(0.2)
        return None

# Função para ver extrato
def ver_extrato(conta):
    print(f"\nExtrato da conta de {clientes[conta]['nome']}:")
    time.sleep(0.2)
    print(f"Saldo: R$ {clientes[conta]['saldo']:.2f}")
    time.sleep(0.2)

# Função para fazer depósito
def fazer_deposito(conta):
    valor = float(input("Digite o valor para depósito: R$ "))
    time.sleep(0.2)
    if valor > 0:
        clientes[conta]['saldo'] += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        time.sleep(0.2)
    else:
        print("Valor inválido para depósito!")
        time.sleep(0.2)

# Função para fazer saque
def fazer_saque(conta):
    valor = float(input("Digite o valor para saque: R$ "))
    time.sleep(0.2)
    if valor > 0 and valor <= clientes[conta]['saldo']:
        clientes[conta]['saldo'] -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        time.sleep(0.2)
    else:
        print("Valor inválido ou saldo insuficiente!")
        time.sleep(0.2)

# Função principal
def main():
    conta_logada = None

    while True:
        if conta_logada is None:
            conta_logada = acessar_conta()
        else:
            mostrar_menu()
            opcao = input("Escolha uma opção: ")
            time.sleep(0.5)

            if opcao == "1":
                print("Você já está acessado à conta!")
                time.sleep(0.5)
            elif opcao == "2":
                ver_extrato(conta_logada)
            elif opcao == "3":
                fazer_deposito(conta_logada)
            elif opcao == "4":
                fazer_saque(conta_logada)
            elif opcao == "5":
                print("Saindo do sistema...")
                time.sleep(0.5)
                break
            else:
                print("Opção inválida!")

# Executando o sistema
if __name__ == "__main__":
    main()
    