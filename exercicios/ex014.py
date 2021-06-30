temp = int(input(f"1-Celsius/Fahrenheit , 2-Fahrenheit/Celsius "))
tempc = float(input("digite a temperatura "))
if (temp == 1):
    tc = ((tempc * 9) / 5) + 32
    print(f'{tempc}Cº em celsius equivale a {tc:.2f} Fº em Fahrenheit')
elif(temp == 2):
    tf = ((tempc - 32)) * 5 / 9
    print(f'{tempc}Fº em Fahrenheit equivale a {tf:.2f} Cº em celsius')

