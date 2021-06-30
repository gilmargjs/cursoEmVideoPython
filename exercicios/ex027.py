'''programa que leia o nome compĺeto e mostra 
   e mostra em seguida o primeiro eo ultimo nome
   separado
   
   ex:anan maria de souza
   primeiro: ana
   ultimo  : souza'''

#valor digitado pelo usuário
nome = input('digite seu nome:')  
#impressão na tela
print(nome)
#remoção dos espaços iniciais e final na frase
novoNome = nome.split()
#impressã o em tela
print(f'Seu primeiro nome é {novoNome[0]}')
#impressão em tela
print(f'Seu ultimo nome é {novoNome[-1]}')