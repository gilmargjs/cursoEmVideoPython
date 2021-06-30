# crie um programa que leia um numero 
# real e mostre na tela a sua inteira
# ex:digite um numero :6.127
# o numero 6.127 tem a parte interia 6. 
from math import trunc
n = float(input("Digite um Numero! "))
print(f'o Valor digitado foi {n:.2f}\nE a sua porção inteira é {trunc(n)}')
