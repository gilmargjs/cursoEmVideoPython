'''desenvolva um programa que leia seis numeros inteiros e
mostre a soma apenas daqueles que forem pares. se o valor 
digitado for impar desconcidere-o.'''
#variaveis  para adicionar valor e contagem 
soma = 0
cont = 0
#loop com range para pedir o valor e repitir por 6 vezes
for c in range(1,7):
    num = int(input(f'Digite o valor {c} valor: '))
    if num % 2 == 0:
#acrecentando os valores e contagem
        soma+=num
        cont+= 1
print(f'Voçê informou {cont} numeros pares e a soma foi :{soma}')
