dia = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM rodados? "))
kmr = 0.15*km
diaria = 60*dia
total = kmr + diaria
print(f'em {dia} dias rodados e percorrendo {km}km o valor do alugueu foi R$ {total:.2f}')