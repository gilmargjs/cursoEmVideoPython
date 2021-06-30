# o professor quer sortear um dos seus quatro aluno 
# para apagar o quadro. faça um programa que ajude ele, 
# lendo o nome deles e escrevendo o nome do escolhido
from  random import choice

a1 = str(input("Nome do Aluno 1: "))
a2 = str(input("Nome do Aluno 2: "))
a3 = str(input("Nome do Aluno 3: "))
a4 = str(input("Nome do Aluno 4 "))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print(escolhido)