'============= MINHA FORMA DE FAZER ============== '
'''crie um programa que faça o computador jogar jokenpô com voçê '''

from  random import randint
from time import sleep
lista = ['pedra','papel','tesoura']

print('-='*20)
print('JOGO DO JOKENPÔ')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-='*20)
jogador = int(input('JOGAR:'))
pc = randint(0,2)
print('po')
sleep(1)
print('ken')
sleep(1)
print('to!!!')
print(f'Voçê jogou {lista[jogador]}') 
print(f'Eo pc jogou {lista[pc]}')
if pc == 0 and jogador == 2 or pc == 2 and jogador == 1 or pc == 1 and jogador == 0:
    print('pc ganhou')
elif jogador == 0 and pc == 2 or jogador == 2 and pc == 1 or jogador == 1 and pc == 0:
    print('você ganhou')
elif jogador == 0 and pc == 0 or jogador == 2 and pc == 2 or jogador == 1 and pc == 1:
    print('o jogo foi empate')
else:
    print('numero invalido')
print('-='*20)


