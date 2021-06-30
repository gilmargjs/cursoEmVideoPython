pro = float(input("Qual o preço do produto R$: "))
pf = pro - (pro * 5 /100)
print(f'O produto que custava  R$ {pro}\nna promoção Com 5% de Desconto ficará por R${pf:0.2f}')