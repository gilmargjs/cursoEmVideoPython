n1 = int(input("Digite o Primeiro Número: "))
n2 = int(input("Digite o Segundo Número: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2

print(f'O Valor Digitado foi {n1} e {n2}')
print(f'A Soma entre {n1} e {n2} é Iguel a {s}')
print(f'A Multiplicação entre {n1} e {n2} é {m}')
print(f'A Divisão entre {n1} e {n2} é {d:0.2f}')
print(f'A Divisão inteira entre {n1} e {n2} é {di}')
print(f'O Resto da Divisão inteira entre {n1} e {n2} é {rd}')
