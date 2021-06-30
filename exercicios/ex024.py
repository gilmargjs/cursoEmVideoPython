'''program que mostra o  nome da cidade e verifique 
   se tem  a palavra comerça com santo '''

#valor digotado pelo usuário
cidade = str(input("Nome da Cidade "))
#impressão na tela 
print(cidade)
#conversão para minusculo e divisão da frase 
novaCidade = cidade.lower().split()
#condição  para imprimir se verdadeiro ou falso
if(novaCidade[0]== 'santo'):
   print(novaCidade[0]== 'santo')
   print('Esta cidade comerça com a palavra santo')
else:
   print(novaCidade[0]== 'santo')
   print('Esta cidade não comerça com a palavra santo')