#Perguntando ao Usuário qual tabuada ele deseja consultar:
tabuada = int(input('Qual número da tabuada você deseja consultar ?'))
for i in range(1,11):
   result = tabuada * i 
   print(f'{tabuada} X {i} = {result}')