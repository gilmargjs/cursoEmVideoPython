'''desenvolva um programa que leia o primeiro termo  ea razão de um PA
no final, mostre os 10 primeiros termos dessa progressão'''
#valor inserido pelo usuario 
primeiro = int(input('primeiro termo: '))
razao = int(input('razão: '))
#formula do decimo termo
decimo = primeiro + (10-1)*razao
#condição
for c in range(primeiro,decimo + razao,razao):
    print(f'{c}',end=' -> ')
print('acabou')