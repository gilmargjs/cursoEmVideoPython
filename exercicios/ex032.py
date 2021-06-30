'''programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

#VALOR DIGITADO PELO USUÁRIO
print('ANO BISSEXTO')
print('='*32)
ano = int(input('ANO:'))
print('='*32)

#CONDIÇÃO
if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
    print(f'O ANO {ano} É UM ANO BISSEXTO')
else:
    print(f'O ANO {ano} NÃO É UM ANO BISSEXTO')
print('='*32)
