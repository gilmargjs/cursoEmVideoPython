def titulo(msg):
    print(msg)
    print('-'* 20)

titulo('Controle de Terrenos')

def area():
    x = float(input('LARGURA (m):'))
    y = float(input('COMPRIMENTO (m):'))
    s = x * y

    print(f'A área do terreno {x} x {y} é de {s}')

area()
