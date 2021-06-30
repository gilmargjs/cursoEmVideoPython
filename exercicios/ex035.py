''' PROGRAMA QUE LEIA O COMPRIMENTO DE TRêS RETAS 
E DIGA AO USUÁRIO SE ELAS PODE FORMA UM TRIÃNGULO OU NÃO . '''
#impressão do cabeçalho
print('=-='*20)
print('ANALISADOR DE TRIÂNGULOS ')
print('=-='*20)
#valor digitado pelo usuário
r1 = float(input("PRIMEIRO SEGMENTO: "))
r2 = float(input("SEGUNDO SEGMENTO: "))
r3 = float(input("TERCEIRO SEGMENTO: "))
print('=-='*20)
#condição 
if(r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print(f'OS SEGMENTOS {r1}, {r2}, {r3} FORMAM UM TRIÂNGULO')
else:
    print(f'OS SEGMENTOS {r1}, {r2}, {r3} NÃO FORMAM UM TRIÂNGULO')
print('=-='*20)
