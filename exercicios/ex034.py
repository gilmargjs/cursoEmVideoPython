''' PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.

PARA SALÁRIO SUPERIOR A R$1250,00. CALCULE UM AUMENTO DE 10%

PARA OS INFERIORES OU IGUAL O AUMENTO E DE 15%.   '''


print('='*30)
print('SALARIO CALCULADO COM AUMENTO')
print('='*30)

#VALOR PASSADO PELO USUÁRIO
sal = float(input('SALARIO BRUTO R$ '))
#CONDIÇÃO
if(sal > 1250):
    print(f'O SEU SALARIO DE R$ {sal} COM 10% DE AUMENTO FICARÁ EM R$ {sal*1.10:.2F}')
elif(sal <= 1250):
    print(f'O SEU SALARIO DE R$ {sal} COM 15% DE AUMENTO FICARÁ EM R$ {sal*1.15:.2F}')
