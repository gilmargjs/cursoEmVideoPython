'''programa que leia dois numeros inteiros e compare-os
mostrando na tela uma mensagem:

- o primeiro valor é maior 
- o segundo valor é maior 
- não existe valor maior,os
dois são iguais '''
print('=:='*15)
num1 = int(input("primeiro numero: "))
num2 = int(input("segundo numero: "))
print('=:='*15)

if num1 > num2:
    print('O primeiro éo valor maior ')
elif num2 > num1:
    print('O segundo éo valor maior')
else:
    print('Não existe valor maior, os dois são iguais')
print('=:='*15)

