'''programa que leia o ano de nascimento de um jovem e informe
de acordo com a sua idade:

-se ele ainda vai se alistar ao serviço militar
-se é a hora de se alistar
-se já passou do tempo do alistamento

seu programa tambem deverá mostrar o tempo que falta ou que passou
do prazo.'''
from datetime import date
atual = date.today().year
print('=:='*15)
nascido = int(input("Data de Nascimento: "))
idade = atual-nascido
ano = nascido+18
print('=:='*15)
print(f'QUEM NASCEU EM {nascido} tem {idade}')
if idade < 18:
    print(f'VOCÊ VAI SE ALISTAR EM  {ano} FALTAM {nascido-atual+18} ANOS')
elif idade > 18:
    print(f'VOCÊ JÁ DEVERIA TER SE ALISTADO EM {ano} PASSARAM {atual-ano} ANOS')
elif idade == 18:
    print(f'ESTÁ NA HORA DE SE ALISTAR SERÁ AGORA EM {ano}')
print('=:='*15)
