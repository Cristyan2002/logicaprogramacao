from random import randint
cpu = randint(1,10)
usuario = int(input('Pensei em um número, dúvido você adivinhar!.'))

while usuario < cpu:
    print('Você não acertou, pensei em um número maior.')
while usuario > cpu:
    print('Você não acertou, pensei em um número menor.')
