'''faça um programa que leia o peso de cinco pessoas.
no final ,mostre qual foi o maior eo menor peso lidos.'''

print('-'*30)
#variavel para armazenar valores
maior = 0
menor = 0
#condição
for p in range(1,6):
#valor inserido pelo usuario
    peso = int(input(f'peso da {p} pessoa: '))
#valor inicial acrecentado nas duas variaveis
    if p ==1:
        maior = peso
        menor = peso
    else:   
#valores trocas em cada variavel para mais e para menos
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    print('-'*30)
print(f'o maior peso foi {maior}kg')
print(f'o menor peso foi {menor}kg')
