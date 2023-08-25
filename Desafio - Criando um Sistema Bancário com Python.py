'''
Hugo de Oliveira fante
github.com/DSHugo

Depósito:
Deve ser possível depositar valores positivos para minha conta bancária.
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
nos preocupar em identificar qual é o número da agência e conta bancária.
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação
de extrato.

Saque:
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00
por saque. CAso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem
informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques
devem ser armazenados em uma varável e exibidos na operação de extrato.

Extrato:
Essa operação dele listar todos os depósitos e saques realizados na conta. No fim da
listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx

Exemplo:
1500.45 = R$ 1500.45
'''
import os

opcao = 0
limite_diario_user = 3
saque_diario_user = 0
saldo = 0
op_deposito = 0
deposito_efetuado = 0
op_saque = 0
saque_efetuado = 0

while True:
    opcao = input('''
-------- MENU --------
Selecione uma opção:

[1] Saque
[2] Depósito
[3] Extrato

----------------------
''')

    if opcao == "1":
        os.system('cls')
        if saque_diario_user == limite_diario_user:
            print("Você atingiu seu limite diário de saque, volte outro dia (ou reinicie o programa :-D)")
            input("")
            os.system('cls')  

        else:
            op_saque = int(input("Digite o valor a ser sacado: "))
            if op_saque > saldo:
                print("Saldo insuficiente...")
                input("")
                os.system('cls')

            elif op_saque <= 0: 
                os.system('cls')
                print("Digite um valor real...")
                input('')

            else:
                os.system('cls')
                saldo -= op_saque
                saque_diario_user += 1
                print("Saque foi realizado!")
                input('')
                os.system('cls')
        

    elif opcao == "2":
        os.system('cls')
        op_deposito = float(input("Digite um valor de até R$ 500, valores decimais deve ser utilizado '.': "))

        if op_deposito >0 and op_deposito <= 500:
            saldo += op_deposito
            deposito_efetuado += 1
            os.system('cls')
            print("Valor depositado na conta com sucesso!")
            input("")
            os.system('cls')
        
        else:
            os.system('cls')
            print("A transação não pode ser concluída, digite um valor disponível")
            input("")
            os.system('cls')

    elif opcao == "3":
        os.system('cls')
        print(f"""
-------- IMPRIMINDO --------
              
Limite diário de saques: {limite_diario_user}
Saques efetuados hoje: {saque_diario_user}  
Depósitos efetuados hoje: {deposito_efetuado}    
Saldo: R$ {saldo:.2f}   
  
----------------------------   
""")
        input("")
        os.system('cls')

    else:
        os.system('cls') 
        print('Opção Inválida...')
        input('')
        os.system('cls')
