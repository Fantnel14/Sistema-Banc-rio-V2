menu = """
======================================
[d]🏦 Depositar
[s]💸 Sacar
[e]📜 Extrato
[u]👤 Criar Usuário
[c]🔒 Criar Conta Corrente
[q]❌ Sair
======================================
=> """

saldo = 0
extrato = []
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas_corrente = []
numero_conta = 1

def deposito(valor):
    global saldo
    print("🏦========= Depósito =========🏦")
    extrato.append(str(valor))
    saldo += valor

def saque(*, saldo, numero_saques):
    global LIMITE_SAQUES
    print("💸========= Saque =========💸")
    saque_valor = float(input("Qual é o valor que deseja sacar?\n=>"))
    if saldo >= saque_valor > 0:
        numero_saques += 1
        if numero_saques > LIMITE_SAQUES:
            print("Uso diário atingido! Retorne amanhã.")
        else:
            extrato.append(str(-saque_valor))
            saldo -= saque_valor
    else:
        print("Valor de saque inválido ou saldo insuficiente.")
    return saldo, numero_saques

def mostrar_extrato(saldo, *, numero_saques=0):
    print("📜========= Extrato =========📜")
    if len(extrato) == 0:
        print("Nenhuma operação realizada ainda.")
    else:
        print(extrato)
    print(f"Saldo: R${saldo:.2f}")

def criar_usuario():
    print("👤========= Criar Usuário =========👤")
    opcao = input("Escolha uma opção:\n[v] Verificar usuários existentes\n[c] Criar novo usuário\n=> ")

    if opcao.lower() == "v":
        if usuarios:
            print("Usuários existentes:")
            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}, CPF: {'*' * 9 + usuario['cpf'][-3:]}")
        else:
            print("Não há usuários existentes.")
    elif opcao.lower() == "c":
        nome = input("Nome do usuário: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF do usuário: ")

        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                print("CPF já cadastrado. Um usuário com este CPF já existe.")
                return

        endereco = input("Endereço (logradouro, nro - bairro - cidade/estado): ")

        novo_usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
        usuarios.append(novo_usuario)
        print("Usuário criado com sucesso!")

def criar_conta_corrente():
    global numero_conta
    print("🔒========= Criar Conta Corrente =========🔒")
    opcao = input("Escolha uma opção:\n[v] Verificar contas existentes\n[c] Criar nova conta\n=> ")

    if opcao.lower() == "v":
        if contas_corrente:
            print("Contas existentes:")
            for conta in contas_corrente:
                print(f"Número da conta: {conta['numero_conta']}, CPF do titular: {'*' * 9 + conta['usuario']['cpf'][-3:]}")
        else:
            print("Não há contas existentes.")
    elif opcao.lower() == "c":
        cpf = input("CPF do titular da conta: ")

        titular_encontrado = None
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                titular_encontrado = usuario
                break
        else:
            print("Usuário com este CPF não encontrado.")
            return

        nova_conta_corrente = {"agencia": "0001", "numero_conta": numero_conta, "usuario": titular_encontrado}
        contas_corrente.append(nova_conta_corrente)
        numero_conta += 1
        print(f"Conta corrente criada com sucesso! Número da conta: {nova_conta_corrente['numero_conta']}")

while True:
    opcao = input(menu)
    if opcao.lower() == "d":
        deposito_valor = float(input("Qual é o valor do depósito?\n=>"))
        deposito(deposito_valor)
    
    elif opcao.lower() == "s":
        saldo, numero_saques = saque(saldo=saldo, numero_saques=numero_saques)
    
    elif opcao.lower() == "e":
        mostrar_extrato(saldo, numero_saques=numero_saques)

    elif opcao.lower() == "u":
        criar_usuario()
    
    elif opcao.lower() == "c":
        criar_conta_corrente()

    elif opcao.lower() == "q":
        break
    else:
        print("Operação inválida! Por favor, selecione outra")
