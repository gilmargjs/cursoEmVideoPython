'''crie um programa que leia o ano de nascimento de sete pessoas. 
No final mostre quantas pessoas ainda não atingiram a maioridade 
e quantas já são maiores'''
from datetime import date
print('-'*30)
#variavel para armazenar valor
maior = 0
menor = 0
#condição
for i in range(1,8):
#variavel para receber contagem
    ano = int(input(f'Ano de nasciento de {i} pessoa '))
    idade = date.today().year-ano
    if (idade >= 18):
        maior = maior + 1
    elif (idade < 18):
        menor = menor + 1
print(f'são {menor} pessoas menores \nE {maior} pessoas maiores de idade')
print('-'*30)
