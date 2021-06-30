'''program que faça o pc pensar em um numero interio 
entre 0 e 5 e peça pra o usuario tentar descobrir o resultado
  
o programa deverá escrever na tela se o usuario ganhou ou perdeu '''
#importando biblioteca 
print('='*30)
print("---ADIVINHA O NÚMERO---")
print('='*30)
from random import randint
#valor digitado pelo usuário
num = int(input("Descubra o número entre 0 e 5: "))
#valor aleatório escolhido pelo pc
num1 = randint(0,5)
#condicional
if(num == num1):
    print(f'O número escolhido pelo PC foi {num1},e o seu foi {num},voçê ganhou')
elif(num != num1 and num):
    print(f'o número ecolhido pelo pc foi {num1},e seu foi {num},voçê perdeu')
    if(num > 5):
        print('NÚMERO MAIOR QUE 5 --INVALIDO-- ')
    elif(num < 0):
        print("NÚMERO MENOR QUE 0 --INVALIDO-- ")

print('='*30)
