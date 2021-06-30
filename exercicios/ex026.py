'''programa que ler uma frase qualquer
   e retorna quantas letras A TEM
   
   -em que posição aparece a primeira vez
   -em que posição aparece a ultima vez
   '''
# valor digitado pelo usuário e convertido para maisculo e 
# retirados os espaços do comerço e fim da frase
frase = input("Digite a Frese! ").upper().strip()
# impressão com contagem da letra A
print('A letra A aparece {} Vezes na frase'.format(frase.count('A')))
#impressão com local da primeira letra A
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
#impressão com local da ultima letra A
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))   