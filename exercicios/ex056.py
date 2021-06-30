'''desenvolva um programa que leia o nome,idade 
  e sexo de 4 pessoas. no final do programa mostre.

  - a media de idade do grupo
  - qual éo nome do homem mais velho.
  - quantas mulheres tem menos de 20 anos.'''

#valor digitado pelo usuario
nomes = []
idades = []
for i in range(1,5):
  print(f'------{i}ºpessoa------')
  nome = str(input(f'PESSOA: '))
  print(f'------{i}ºIDADE-------')
  idade = int(input(f'IDADE: '))
  print(f'------{i}ºSEXO-------')
  sexo = str(input('SEXO [M/F]: '))
  nomes.append(nome)
  idades.append(idade)
print(nomes)
print(idades)
