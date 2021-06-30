# faça um programa que leia um trianguilo
# qualquer e mostre na tela o valor do seno ,coseno e tangente.
import math 
ang = float(input("Informe um angilo "))
print(f'Em um Angulo de {ang} graus o seno é {math.sin(math.radians(ang)):.2f}\nO coseno é {math.cos(math.radians(ang)):.2f}\nE a tangente é {math.tan(math.radians(ang)):.2f}')
