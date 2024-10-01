# Fazendo um exercícios de tuplas e acessando informações dessa tupla.
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'São Paulo', 'Fluminense', 'São Paulo', 'Fortaleza.', 'Chapecoense', 'Goiais')

# Fazendo o Print acessar somente os cincos primeiros times.
print('Os primeiros times são: {} '.format(times[0:5]))
print('Os Ultimos times são:{} '.format(times[::-1][:4]))
times_alfabeticos = sorted(times)
print('Os times em ordem alfabética fica: {}'.format(times_alfabeticos))
print('O Chapecoense está na posição {}'.format(times.index('Chapecoense')+1))

