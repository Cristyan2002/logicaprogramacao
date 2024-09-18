frase = input('Digite uma frase')
contagem_vogal = 0
vogal = 'AaEeIiOoUu'
for lista in frase:
    if lista in vogal:
        contagem_vogal += 1
print(contagem_vogal)
