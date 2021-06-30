'''faça um programa que mostre na tela uma contagem regressiva para o estouro de 
fogos de artificio. indo de 10 até 0,com uma pausa de 1 segundo entre elas.
'''
ESTOUROU = ('''    
   ----------------------------
    \\\\\FELIZ ANO NOVO!//////
   ----------------------------    
   ''')
from time import sleep
# versão com while
# contagem = 10
# while contagem > 0:
#     print(f'CONTAGEM: {contagem}')
#     sleep(1)
#     contagem = contagem - 1
# print(ESTOUROU)

for i in range(10,-1,-1):
    print(f'CONTAGEM: {i}')
    sleep(1)
print(ESTOUROU)