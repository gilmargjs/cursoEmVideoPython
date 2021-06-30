'''refaça o desafio ex035 dos triangulos, acrecentando o recurso de mostrar que tipo de triangulo será formado

-EQUILÁTERO todos os lados iguais
-ISÓSCELES dois lados iguais
-ESCALENO todos os lados diferentes

 PROGRAMA QUE LEIA O COMPRIMENTO DE TRêS RETAS E DIGA AO USUÁRIO SE ELAS PODE FORMA UM TRIÃNGULO OU NÃO . '''
#impressão do cabeçalho
print('--'*20)
print('ANALISADOR DE TRIÂNGULOS ')
print('--'*20)
#valor digitado pelo usuário
r1 = float(input("PRIMEIRO SEGMENTO: "))
r2 = float(input("SEGUNDO SEGMENTO: "))
r3 = float(input("TERCEIRO SEGMENTO: "))
print('--'*20)
#condição 
if(r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print(f'OS SEGMENTOS {r1}, {r2}, {r3} FORMAM UM TRIÂNGULO',end='')#end coloca a proxima linha na sequencia
    if (r1 == r2 and r2 == r3 ):
        print('TRIANGULO EQUILATERO')
    elif (r1 != r2 and r2 != r3 and r1 != r3):  
        print('TRIANGULO ESCALENO')
    else:
        #pela complexidade do codigo fica melhor deixar este segmento no else.
        #ex:  if a == b and b != c and b == c and a != c and a == c and b != a: 
        print('TRIANGULO ISÓSCELES')
else:
    print(f'OS SEGMENTOS {r1}, {r2}, {r3} NÃO FORMAM UM TRIÂNGULO')
print('--'*20)