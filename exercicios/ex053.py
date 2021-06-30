'''crie um programa que leia uma frase qualquer e diga se ela é
um palindromo,desconsiderando os espaços

ex: apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''
print('ANALISAR SE A FRASE')
print('-'*30)
#valor digitado pelo usuario
frase = str(input('Digite a Frase:')).upper()
#retirada dos  espaços da direita e esquerda
frase1 = frase.split()
#juntando todos os itens da frase
nova = ''.join(frase1)
#invertendo a frase junta
nova1 = nova[::-1]
#verificar se a frase é um palindromo
print('-'*30)
print(f'O inverso de {frase} é {nova1}')
if nova == nova1:
    
    print('é um palindromo')
else:
    print('não é um palindromo')
    print('-'*30)
