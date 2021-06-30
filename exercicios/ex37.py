"""programa que laeia um número intgeiro qualquer e peça
para o usuario escolher qual será a base da conversão:

-1 para binario
-2 para octal
-3 para hexadecimal
"""
print('='*30)
print('SISTEMA DE CONVERÇÃO DE BASES')
print('='*30)

num = int(input("Digite um número: "))
print('''Escolha uma das Bases para Conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
print('='*30)

opcao = int(input("Sua Opção: "))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('escolha uma opção valida')
print('='*30)
