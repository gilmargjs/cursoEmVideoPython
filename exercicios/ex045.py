from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual éa sua jogado? '))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po!!!')
print('-='*13)
print(f'O computador jogou: {itens[computador]} ')
print(f'O jogador  jogou: {itens[jogador]} ')
print('-='*13)
if computador == 0:#pedra
    if jogador == 0:
        print('jogo empatou')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:#papel
    if jogador == 0:
        print('computador venceu')
    elif jogador == 1:
        print('jogo empatou')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:#tesoura
    if jogador == 0:
        print('jogador venceu')
    elif jogador == 1:
        print('computador venceu')
    elif jogador == 2:
        print('jogo empatou')
    else:
        print('JOGADA INVALIDA!')