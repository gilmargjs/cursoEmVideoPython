'''programa para aprovar o emprestimo bancario para compra de uma casa. 
o programa vai perguntar o valor da casa, o salario do comprador e em 
quantos anos ele vaia pagar. 

calcule o valor da prestação mensal. sabendo que ele não pode 
exceder 30% do salario ou então o emprestimo será negado '''

print('--=--'*10)
print('FINACIAMENTO DA CASA PROPRIA')
print('--=--'*10)
#VALOR DIGITADO PELO USUARIO
valor = float(input('VALOR TOTAL DA CASA R$: '))
salario = float(input('SALARIO BRUTO R$: '))
ano = int(input("TEMPO ESTIMADO DO FINANCIAMENTO ANOS: "))
meses = ano*12
print('--=--'*10)
print("ATENÇÃO COMPROMETER ATÉ 30% DO SALARIO")
prestacao = valor/meses
limite = salario*30/100
porcento =100*(prestacao/salario)
if(prestacao<=limite):
    print(f'R$ {valor} em {ano} anos a prestação fica R$ {prestacao:.2f} que é {porcento:.2f}% do seu salario \nEMPRESTIMO APROVADO')
else:
    print(f'R$ {valor} em {ano} anos a prestaçaõ fica R$ {prestacao:.2f} que é {porcento:.2f}% do seu salario \nEMPRESTIMO NEGADO')
print('--=--'*10)


