import math

new = input()

if len(new)==3:
    n = int(new[0])
    k = int(new[2])
    print(n)
    print(k)
    if n == 1 or n == k:
        print(1)
    if k > n:
        print(0)
    else:
        x = math.factorial(n)
        y = math.factorial(k)
        sym = x//(y*(n-k))
        print((sym))
elif len(new)==5:
    n = int(new[0]+new[1])
    k = int(new[3]+new[4])
    if n == k:
        print(1)
    if k > n:
        print(0)
    else:
        x = math.factorial(n)
        y = math.factorial(k)
        sym = x//(y*(n-k))
        print((sym))
else:
    print(0)
