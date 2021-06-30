def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores{valores} temos {s}')

soma(6,5,6)
soma(5,9,8,6,3)