calculo_idade = 0
idade_maior = 0
nome_maior = 0
mulher_idade = 0
for i in range(1,5):
    print(f'------{i}ª PESSOA------')
    p = str(input('NOME: '))
    idade = int(input('IDADE:'))
    s = str(input('SEXO: M/F: ')).upper()
    calculo_idade = calculo_idade + idade
    if idade > idade_maior:
        idade_maior = idade
        nome_maior = p
    if s == 'F' and idade <20:
        mulher_idade += 1
print('A média de idade do grupo é {}'.format(calculo_idade / 4))
print('A maior idade deste grupo é {} e seu nome é {}'.format(idade_maior, nome_maior))
print('São {} Menores de 20 Anos'.format(mulher_idade))


