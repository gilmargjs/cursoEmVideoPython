# o mesmo professor que  quer sortear a ordem
# de apresentação dos trabalhos dos alunos
# programa para ler o nome dos quatro e mostrar
# na tela a ordem sorteada.
from random import shuffle 

a1 = str(input("nome 1 "))
a2 = str(input("nome 2 "))
a3 = str(input("nome 3 "))
a4 = str(input("nome 4 "))

lista = [a1, a2, a3, a4]
escolha = shuffle(lista)
print(escolha)
