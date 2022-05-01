import math


def ile_symbol(n,k):
#    if len(symbol) == 3:
#        n = symbol[0]
#        k = symbol[2]
    x = math.factorial(n)
    y = math.factorial(k)
    z = math.factorial(n-k)
    wynik = x/(y*z)
    return wynik
#    elif len(symbol) == 5:
#        n = int(symbol[0] + symbol[1])
#        k = int(symbol[3] + symbol[4])
#        x = math.factorial(n)
#        y = math.factorial(k)
#        z = math.factorial(n-k)
#        wynik = x / (y * z)
#        return wynik

symbol = input()
if len(symbol) == 3:
    n = symbol[0]
    k = symbol[2]
elif len(symbol) == 5:
    n = int(symbol[0] + symbol[1])
    k = int(symbol[3] + symbol[4])
wynik=ile_symbol(n,k)
print(wynik)



