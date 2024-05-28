menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [uc] Cadastrar usuário
    [ac] Criar conta
    [vc] Listar contas
    [vu] Listar usuários
##############################
"""

usuarios = []
contas = []
PREFIXO_CONTA = "0001"
numero_conta = 0
saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def cadastrar_usuario(usuarios):
    nome = input("Nome:")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa):")
    cpf = input("CPF:")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado)")
    if any(usuario[2] == cpf for usuario in usuarios):
        print("Usuário já existente")
        return False
    else:
        usuarios.append([nome, data_nascimento, cpf, endereco])
        print("Cadastro feito com sucesso!")
        return True

def criar_conta(contas):
    global numero_conta
    cpf = input("CPF:")
    for i in range(len(usuarios)):
        if usuarios[i][2] == cpf:
            numero_conta += 1
            contas.append([PREFIXO_CONTA, numero_conta, usuarios[i]])
            print("Conta criada com sucesso!")
            return True
    print("CPF não identificado")
    return False
            

def deposito(saldo, valor, extrato, /):
    if(valor > 0):
        print("Depósito recebido com sucesso!")
        saldo += valor
        extrato += f"""
    Depósito recebido de R$ {valor:.2f}
----------------------------------------
"""
        return saldo, extrato
    else:
        print("Não é aceito operação com números negativos")

def saque(*, saldo, extrato, numero_saques, valor, LIMITE, LIMITE_SAQUES):
    if(valor <= saldo and valor <= 500 and numero_saques < LIMITE_SAQUES and valor > 0):
        saldo -= valor
        print("Saque realizado com sucesso!")
        numero_saques += 1
        extrato += f"""
    Saque realizado de R$ {valor:.2f}
----------------------------------------
"""
    
    elif(valor > saldo):
        print(f"O valor disponível é de R$ {saldo:.2f}")

    elif(valor > 500):
        print("O valor máximo de saque é de R$ 500.00")

    elif(valor < 0):
        print("Não é aceito operação com números negativos")

    else:
        print("Você já atingiu o limite de saques no dia")

    return saldo, extrato

def print_extrato(saldo, /, *, extrato):
    print("Extrato")
    print(extrato)
    print(f"Valor em conta: R$ {saldo:.2f}")

while True:
    opcao = input(menu)

    if opcao == "uc":
        print("Cadastrar usuário")
        cadastrar_usuario(usuarios)

    elif opcao == "ac":
        print("Cadastrar conta")
        criar_conta(contas)

    elif opcao == "d":
        print("Depósito")
        saldo, extrato = deposito(saldo, float(input()), extrato)

    elif opcao == "s":
        print("Saque")
        saldo, extrato = saque(saldo = saldo, extrato = extrato, numero_saques = numero_saques, valor = float(input("Valor a sacar:")), LIMITE = LIMITE, LIMITE_SAQUES = LIMITE_SAQUES)

    elif opcao == "e":
        print_extrato(saldo, extrato = extrato)


    elif opcao == "q":
        break

    elif opcao == "vc":
        for i in range(len(contas)):
            print(contas[i])

    elif opcao == "vu":
        for i in range(len(usuarios)):
            print(usuarios[i])

    else:
        print("Operação inválida, por favor, selecione novamente a opção desejada.")