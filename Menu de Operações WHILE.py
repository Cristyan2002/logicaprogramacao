from time import sleep
print('Olá, Bem-Vindo ao MENU DE OPERAÇÕES!')
soma1 = int(input('Digite o primeiro número: '))
soma2 = int(input('Digite o segundo número: '))
while True:
    escolha = int(input('Escolha uma das operações: \n [1] Somar \n [2] Multiplicar \n [3] Subtrair \n [4] Digitar novos números \n [5] Qual é o maior \n [6] Sair do menu de operações: \n'))
    if escolha == 1:
        print('O resultado do número {} + {} é = {}'.format(soma1, soma2, soma1+soma2))
        sleep(2)
    elif escolha == 2:
        print('O resultado do número {} x {} é = {}'.format(soma1, soma2, soma1*soma2))
        sleep(2)
    elif escolha == 3:
        print('O resultado do número {} - {} é = {}'.format(soma1, soma2, soma1-soma2))
        sleep(2)
    elif escolha == 4:
        print('Olá, Bem-Vindo ao MENU DE OPERAÇÕES!')
        soma1 = int(input('Digite o primeiro número: '))
        soma2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        if soma1 > soma2:
            print('O primeiro número é maior que o segundo! PRIMEIRO: {} SEGUNDO: {}'.format(soma1,soma2))
        elif soma1 == soma2:
            print('Os dois números tem o mesmo valor!')
        else:
            print('O segundo número digitado é maior que o primeiro! PRIMEIRO: {} SEGUNDO {}'.format(soma1,soma2))
        sleep(2)
    elif escolha == 6:
        print('Ok, saindo do menu de operações!')
        sleep(1)
        break
    else:
        print('Você escolheu um número que não existe na opção, tente novamente.')
        sleep(2)

