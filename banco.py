menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
        
        else:
            print("Operação não efetuada! Pois o valor informado é inválido.")
            
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação não efetuada! Pois você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação não efetuada! Pois o valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação não efetuada! Pois o número de saques excede o limite máximo permitido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação não efetuada! Pois o valor informado é inválido.")
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
            
    elif opcao == "4":
        break
        
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada")   