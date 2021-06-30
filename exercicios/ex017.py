# faça um programa que laiea
# o comprimento do cateto adjacente
# e do cateto oposto de um triagulo
# retangulo, calcule e mostre a sua 
# hipotenusa
from math import hypot
n1 = float(input("cateto adjacente "))
n2 = float(input("cateto oposto "))
print(f'o triangulo com o cateto adjacente {n1}\neo cateto oposto {n2}\ntem uma hipotenusa com valor {hypot(n1,n2):.2f}')