'''faça um programa que calcule a  soma entre todos o numeros 
que são multiplos de três e que se encontram no intervalo de 1 até 500 '''
#variavel para contar 
soma = 0
cont = 0
#laço para imprimir numeros impares
for i in range(1, 501,2):
#retorno dos nomeros divisiveis por 3
    if i % 3 == 0:
#variavel para acumular os numeros de valores
        cont += 1
#variavel para receber os valores somados
        soma += i
#impressão do valor
print(f'A Soma de todos os {cont} valores é {soma}')