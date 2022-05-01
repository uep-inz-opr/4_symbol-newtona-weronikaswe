import math

new = input()
n = int(new[0])
k = int(new[2])

if n == 1 or n == k:
    print(1)

if k > n:
    print(0)
else:
    x = math.factorial(n)
    y = math.factorial(k)
    sym = x//(y*(n-k))
    print((sym))
    