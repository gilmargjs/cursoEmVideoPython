'''programa que leia duas notas e calcule sua media. 
mostrando uma mensagem nofinal de acordo com a media:

-media abaixo de 5.0 REPROVADO
-media entre 5.0 e 6.9 RECUPERAÇÃO
-media 7.0 ou superior APROVADO
'''
print('MÉDIA DO ALUNO')
print('=:='*15)
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
print('=:='*15)
print('''
...ATENÇÃO...
A  BAIXO DE 5.0    REPROVADO
ENTRE 5.0 E 6.9    RECUPERAÇÃO
ACIMA    DE 7.0    APROVADO''')
print('=:='*15)
print(f'SUA NOTA FOI {n1} E {n2} SUA MEDIA FOI {media:.2F}.')

if media < 5.0:
    print('ALUNO REPROVADO')
elif media >= 5.0 and media <=6.9:
    print('ALUNO EM RECUPERAÇÃO')
elif media > 7.0 and media <= 10:
    print('ALUNO APROVADO')
elif media > 10:
    print('DIGITE UM VALOR MENOR QUE 10')
else:
    print('DIGITE UM VALOR VALIDO')
print('=:='*15)
