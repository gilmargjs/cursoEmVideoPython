''' PROGRAMA QUE LEIA TRÊS NUMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR'''
#CABEÇALHO IMPRESSO NA TELA 
print('='*30)
print('VEIRFICAR QUAL O MAIOR NÚMERO')
print('='*30)

#VALOR  INFORMADO PELO USUÁRIO
a = int(input("INFORME O PRIMEIRO NÚMERO: "))
b = int(input("INFORME O SEGUNDO NÚMERO: "))
c = int(input("INFORME O TERCEIRO NÚMERO: "))
print('='*30)

#CONDIÇÃO
#VERIFICANDO QUEM É MAIOR
maior = a
if(b > a and b > c):
    maior = b
if(c>b and c>a):
    maior = c

if(a == b or a == c or b == c):
    print('OS NÚMEROS SÃO IGUaIS')
    
#CONDIÇÃO 2
#VERIFICANDO QUEM É MENOR 
menor = a
if(b<a and b < c):
    menor = b
if(c<b and c<a):
    menor = c
print(f'O MENOR NÚMERO DIGITADO FOI {menor}')
print(f'O MAIOR VALOR DIGITADO FOI {maior}')