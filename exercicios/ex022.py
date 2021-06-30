'''crie um programa que leia um nome completo de uma pessoa
e retorne 
- o nome com todas as letras maiusculas
- quantas letras tem sem os espaços
- quantas letras tem o primeiro nome
'''
nome = str(input("DIGITE SEU NOME: "))  
print(f'Seu nome me Maiusculo é {nome.upper()}')
print(f'Seu nome em Minusculo é {nome.lower()}')
meunome = nome.split()
este = ''.join(meunome)
print(f'Seu nome tem ao todo {len(este)} letras')
print(f'Seu primeiro nome é {meunome[0]} e tem {len(meunome[0])}')
print(f'Seu nome é {este} e tem {len(este[0])}')