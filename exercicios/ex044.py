'''elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

-Avista dinheiro/cheque: 10% de desconto
-avista no cartão: 5% de desconto 
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
'''
#impressõ de cabeçalho
print('--'*20)
print('CALCULO DE PREÇO')
print('--'*20)
print('''FORMA DE PAGAMENTO
[ 1 ] AVISTA DINHEIRO/CHEQUE 10% DESCONTOS
[ 2 ] AVISTA CARTÃO 5% DESCONTOS
[ 3 ] CARTÃO 2X SEM DESCONTO
[ 4 ] CARTÃO 3X 20% JUROS''')
print('--'*20)
#formulas
#valor inserido pelo usuário
preco = float(input('VALOR DO PRODUTO: '))
opcao = int(input('FORMA DE PAGAMENTO: '))
av = preco*10/100
avCartao = preco*5/100
cartao2x = preco
cartao3x = preco*1.20
#condição
if opcao == 1:
    print(f'um produto que custa R${preco} com desconto de 10% ficara por {preco - av:.2f}')
elif opcao == 2:
    print(f'um produto que custa R${preco} com desconto de 5% ficara por {preco - avCartao:.2f}')
elif opcao == 3:
    print(f'um produto que custa R${preco} Não tem desconto')
elif opcao == 4:
    print(f'um produto que custa R${preco} com juros de 20% ficara por {preco + cartao3x:.2f}')
else:
    print('opção invalida')