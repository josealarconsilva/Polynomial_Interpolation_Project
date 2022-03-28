import math

def f(x):
    return 4/(1+x**2)
def trapezoid(f, a, b, n):
    h = (b-a)/n
    result = (0.5)*(f(a)) + (0.5)*f(b)
    for i in range(1, n):
        result = result + f(a + (i*h))
    result = result * h
    print(result)
    print(math.pi - result)

trapezoid(f, 0, 1, 30)