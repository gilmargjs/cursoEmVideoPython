''' programa que pergunte a distancia de uma viagem em km.
calcule o preço da passagem . cobrando R$ 0.50 por km para 
viagens de até 200km. 
- e R$ 0,45 para viagens mais logas  '''
#VALOR INFORMADO PELO USUÁRIO
print('='*50)
print('DIGITE A DISTÃNCIA DA VIAGEM')
print('='*50)
dist = float(input("DISTÂNCIA EM KM:"))
#CONDIÇÃO
if (dist <= 200):
    print(f'O VALOR DA VIAGEM DE {dist}KM É DE R$ {dist*0.50:.2F}')
elif (dist > 200):
    print(f'O VALOR DA VIAGEM DE {dist}KM É DE R$ {dist*0.45:.2F}')
else:
    print('DIGITE UM VALOR VALIDO')
print('='*50)
