'''desenvolva uma logica que leia o peso e a altura de uma pessoa 
calcule o IMC e mostre seu status, de acordo com a tabela a bixo:

-abaixo de 18.5; abaixo do peso 
-entre 18.5 e 25: peso ideal
-25 ate 30: sobre peso
-30 ate 40 obesidade
-acima de 40:obesidade mórbida
 '''
#IMPRESSÃO DO  CABEÇALHO
print('--'*20)
print('CALCULO DO IMC')
print('--'*20)
print('''-abaixo de 18.5; abaixo do peso 
-entre 18.5 e 25: peso ideal
-25 ate 30: sobre peso
-30 ate 40 obesidade
-acima de 40:obesidade mórbida''')
print('--'*20)
#FORMULAS
peso = float(input('PESO (kg): '))
altura = float(input('ALTURA (m): '))
imc = peso/(altura*altura)
print(f'SEU IMC É {imc:.1f} SUA SITUAÇÃO É ',end='')
if imc < 18.5:
    print('ABIXO DO PESO CUIDAD!')
elif imc < 25:
    print('PESO IDEAL PARABENS')
elif imc < 30:
    print('SOBRE PESO CUIDADO!')
elif imc < 40:
    print('OBESIDADE ALERTA!')
else:
    print('OBESIDADE MÓRBIDA PERIGO!')
