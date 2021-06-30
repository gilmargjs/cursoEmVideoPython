'''refaça o desafio 009, mostrando a tabuada de um numero
que o usuario escolher. só que agora utilizando um laço for.'''
n = int(input('tabuada de: '))
for i in range(1,11):
    print(f'{n} x {i:2} = {i*n}')