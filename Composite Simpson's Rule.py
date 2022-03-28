import math
def f(x):
    return 4/(1+x**2)
def simpsons(f, a, b, n):
    h = (b-a)/n
    X = [None]*(n+1)
    X[0] = a
    for i in range(1, n+1):
        X[i] = a + (i * h)
    print(X)
    sum1 = 0
    sum2 = 0
    for i in range(2, math.floor(n/2)):
        sum1 = sum1 + f(X[2*i-2])
    for i in range(1, math.floor(n/2)):
        sum2 = sum2 + f(X[2 * i - 1])
    functval = (h/3)*(f(X[0]) + 2 * sum1 + 4 * sum2 + f(X[n]))
    print(functval)
    print(math.pi - functval)

simpsons(f, 0, 1, 30)