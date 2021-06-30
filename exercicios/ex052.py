'''faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.'''
#valor iserido pelo usuario
n = int(input('Número: '))
#variavel para receber contagem
tot = 0
#laço condicional
for c in range(1,n + 1):
#formula
    if n % c == 0:
        print('\033[33m',end='')
        tot+= 1
    else:
        print('\033[35m',end='')
print(f'\33[m O Número {n} foi Divisivel {tot} vezes ')
#se o numero for divido por 2 numeros é primo
if tot == 2:
    print('e por isso é primo')
else:
    print('e por isso não é primo')