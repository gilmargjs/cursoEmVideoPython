'''PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRA SUA CATEGORIA DE ACORDO COM A IDADE

-ATE 9 ANOS: MIRIM
-ATE 14 ANOS: INFANTIL
-ATE 19 ANOS: JUNIOR
-ATE 20 ANOS: SENIOR
-ACIMA: MASTER

'''
print('--'*15)
print('''CATEGORIA DE ATLETAS
MIRIM     9 ANOS
INFANTIL 14 ANOS
JUNIOR   19 ANOS
SENIOR   20 ANOS
MASTER A CIMA''')
print('--'*15)
from datetime import date
nascido = int(input('ANO DE NASCIMENTO: '))
atual = date.today().year
idade = atual - nascido
print(f'QUEM NASCEU EM {nascido} TEM {idade} ANOS')
if idade <= 9:
    print('E a categoria é MIRIM')
elif idade <= 14:
    print('E a categoria é INFANTIL')
elif idade <= 19:
    print('E a categoria é JUNIOR')
elif idade <=20:
    print('E a categoria é SENIOR')
else:
    print('E a categoria é MASTER')
print('--'*15)