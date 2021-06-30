'''programa que ler o nome e verifica 
   se tem silva no nome'''
print('='*30)
print('VERIFICAR NOME')
print('='*30)
#valor digitado pelo usuario
nome = input("Digite Seu Nome ")
#remoção dos espaços no inicio e fim e conversão para minusculo
meuNome = nome.strip().lower()
#verifiacar se existe a o sobre nome no nome
outro = 'silva' in meuNome
#impressão do valor final na tela
print('Seu nome tem silva?')  
if(outro == True):
   print('SIM')
else:
   print('NÃO')
print('='*30)
