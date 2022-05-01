import math

def ile_symbol(n,k):
    x = math.factorial(n)
    y = math.factorial(k)
    z = math.factorial(n-k)
    wynik = x/(y*z)
    return wynik

symbol = input()
if len(symbol) == 3:
    n = int(symbol[0])
    k = int(symbol[2])
elif len(symbol) == 5:
    n = int(symbol[0] + symbol[1])
    k = int(symbol[3] + symbol[4])
wynik=ile_symbol(n,k)
print(wynik)



