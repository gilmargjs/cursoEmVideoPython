''' programa que leia e mostre na tela um numero inteiro mostre se ele é inpar ou par '''
print('='*50)
print('VERIFICAR NÚMERO')
print('='*50)
#VALOR DIGITADO PELO USUÁRIO
num = int(input("Digite um número: "))
print('='*50)
#CONDIÇÃO
if num % 2 == 0:
    print(f'o número {num} é par')
else:
    print(f'o número {num} é impar')
print('='*50)
