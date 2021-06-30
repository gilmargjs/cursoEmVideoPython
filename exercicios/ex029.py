'''
programa que leia a velocidade de um carro.
- se ultrasar de 80km/h.
- mostrar uma mensagem
dizendo que ele foi multado.
- a multa vai custar R$ 7,00 por cada km acima. '''

#valor digitado pelo usuário
print('='*57)
print("DIGITE A VELOCIDADE DO CARRO")
print('='*57)
velo = int(input("velocidade do carro em km/h "))
#condicional
if(velo > 80):
    print(f'Sua Velocidade está a {velo}km/h,voçê ser multado em R${(velo-80)*7:.2f}')
else:
    print(f'sua velocidade foi {velo}km/h,voçê está dentro do limite de velocidade')
print('='*57)
