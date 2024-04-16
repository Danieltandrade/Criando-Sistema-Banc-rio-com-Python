#Criando um sistema Bancário com Pyhton
#Curso: Python Development
#Instituição: DIO.me
#Instrutor: Guilherme Arthur de Carvalho

boas_vindas = """
BEM VINDO AO BANCO TORRES!

Favor selecionar uma opção abaixo:
"""
print(boas_vindas) # Imprime no terminal mensagem de boas vindas.
# Apresenta menu com opções para seleção.
menu = """         
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

#Declaração de variáveis utilizadas no código.
saldo = 0            # Variável inicializada com zero, representa o saldo da conta do cliente.
limite = 500         # Variável que define o limite máximo para saques (nesse caso, 500).
extrato = ""         # Variável tipo string vazia que será usada para registrar as transações.
numero_saques = 0    # Variável inicializada com zero, conta o número de saques realizados.
LIMITE_SAQUES = 3    # Variável que define o limite máximo de saques permitidos (neste caso, 3).

while True: # Loop principal. Condição permanece verdadeiro até tecla "0" ser pressionada.

    opcao = input(menu)     # Seleção de uma opção.

    if opcao == "1":        # Solicita ao usuário um valor de deposito.
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "2":      # Solicita um valor de saque.
        valor = float(input("Informe o valor do saque: "))

        #Verifica se o valor excede o saldo, o limite ou o número máximo de saques.
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação não realizada! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação não realizada! Número máximo de saques excedido.")

        # Se todas as condições forem atendidas, o valor é subtraído do saldo e registrado no extrato.
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é inválido.")
    # Exibe o extrato das transações realizadas (ou uma mensagem informando que não houve movimentações).
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Encerra o programa com uma mensagem de agradecimento.
    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!0")
        print("Tenha um bom dia!")
        break
    
    # Se o usuário digitar uma opção inválida, uma mensagem de erro é exibida.
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")