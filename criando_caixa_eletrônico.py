menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depósitar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso")

        else:
            print("Operação falhou, o valor informado é inválido.")

    elif opcao == "s":
        saque = float(input("Digite o valor que deseja sacar: "))
        if saque < saldo:
            if saque < limite:
                if numero_saques <= LIMITE_SAQUES:
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    numero_saques += 1
                    print("Saque realizado com sucesso")
                else:
                    print("Operação falhou! Número máximo de saque excedido.")
            else:
                print("Operação falhou! O valor do saque excede o limite.")
        else:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif opcao == "e":
        print("{:=^30}".format(" EXTRATO "))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=" * 30)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
print("{:=^30}".format(" OPERAÇÃO ENCERRADA "))
