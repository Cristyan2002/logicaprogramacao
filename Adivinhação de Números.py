from random import randint
cpu = randint(1,10)
tentativas = 0
while True:
    usuario = int(input('Pensei em um número, dúvido você adivinhar!.'))
    tentativas += 1
    if cpu == usuario:
        print('Você acertou eu pensei no número {}'.format(cpu))
        break
    elif cpu > usuario:
        print('Eu pensei em um número maior!')
    elif cpu < usuario:
        print('Eu pensei em um número menor!')
