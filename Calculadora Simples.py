from time import sleep
print('Olá bem vindo a uma calculadora bem simples!')
def menu_operacoes():
    numero1 = int(input('Digite o primeiro número inteiro: '))
    numero2 = int(input('Digite o segundo número inteiro: '))
    operacao = str(input('SOMA [+]\nSUBTRAÇÃO [-]\nMULTIPLICAÇÃO [*]\nDIVISÃO [/]\nDigite a operação que deseja realizar: '))
    return numero1,numero2,operacao
while True: 
    numero1, numero2, operacao = menu_operacoes()
    
    if operacao == '+':
        resultado = numero1 + numero2
        print('O Resultado do número: {} + {} é {}'.format(numero1,numero2,resultado))
    elif operacao == '-':
        resultado = numero1 - numero2
        print('O Resultado do número: {} - {} é {}'.format(numero1,numero2,resultado))
    elif operacao == '*':
        resultado = numero1 * numero2
        print('O Resultado do número: {} X {} é {}'.format(numero1,numero2,resultado))
    elif operacao == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
            print('O Resultado do número: {} / {} é {}'.format(numero1,numero2,resultado))
        else:
            print('Número divido por 0 não é possivel.')
    while True:
        desejo = str(input('Você deseja continuar com as operações ? [S]/[N]')).upper()
        if desejo == 'S':
            print('Okay, você irá fazer outras novas operações')
            break
        if desejo == 'N':
            print('Você desejou sair!.')
            exit()
        else:
            print('Opção inválida')
            
            
    
    
