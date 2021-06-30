'''faça um programa que leia do numero 0 até 9999 
e mostre na tela cada um dos digitos separados 
ex:
unidade : 0
dezena  : 0
centena : 0
milhar  : 0
'''
#valor digitado pelo o usuário
nu = int(input("Digite um numero: "))
#formula para converter o numero para unidade,dezena,centena,milhar
unidade = nu//1%10
dezena = nu//10%10
centena = nu//100%10
milhar = nu//1000%10
#impressão na tela
print(f'o numero {nu} tem a\nMilhar {milhar}\nCentena {centena}\nDezena {dezena}\nUnidade {unidade}')