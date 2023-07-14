saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "a":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro, digite um valor válido!")

    elif opcao == "b":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Você não tem limite suficiente")

        elif excedeu_saques:
            print("Você não tem saques suficiente")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor informado é inválido.")

    elif opcao == "c":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        break

    elif opcao == "d":
        break
    else:
        print("Operação inválida.")
