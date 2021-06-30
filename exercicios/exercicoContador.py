def contador():
    print('='*30)
    print('contagem de 1 até 10 de 1 em 1')
    print('='*30)

    a = 1
    while a < 11:
        print(a)
        a = a + 1

contador()

def contador1():
    print('='*30)
    print('contagem de 10 até 0 de 2 em 2')
    print('='*30)
    i = 10
    while i > -1:
        print(i)

        i = i - 2

contador1()

def contador3():
    print('='*30)
    print('Agora é a Sua Vez de personalizar a contagem ')
    print('='*30)
    b = int(input('Inicio:'))
    c = int(input('Fim:'))
    d = int(input('Passo:'))
    if(d <= 0):
        d=1
    print(f'contagem de {b} até {c} de  {d} em {d}')
    while b < c:       
        print(b)
        b = b + d

    if(b > c):
        while b > c:
            print(b)
    b = b - d

            
contador3()