import numpy as np
import matplotlib.pyplot as plt
import math


def newtonmethod(x, y, z):
    n = np.shape(y)[0]
    newtontable = np.zeros([n, n])
    for i in range(n):
        newtontable[i][0] = y[i]
    for j in range(1,n):
        for i in range(n-j):
            newtontable[i][j] = (newtontable[i+1][j-1] - newtontable[i][j-1])/(x[i+j]-x[i])
    coefs=[]
    for i in range(n):
        coefs.append(newtontable[0, i])
    n = len(x) - 1
    p = coefs[n]
    for k in range(1, n + 1):
        p = coefs[n - k] + (z - x[n - k]) * p
    return p


def f(c, x):
    return (1 / (c * pow(x, 2) + 1))


def plots(c, n):
    x = [None] * (n+1)
    y = []
    x[0] = 0.1
    for i in range(1, (n+1)):
        x[i] = (math.cos((2*i*math.pi - math.pi)/(2*n)))
    x.sort()
    print(x)
    for i in range(0, n+1):
        y.append(f(c, x[i]))
    print(y)
    y_interpolated = []
    for i in range(0, (n+1)):
        y_interpolated.append(newtonmethod(x, y, x[i]))
        print(y_interpolated)



    r = np.linspace(-1, 1, 100)
    z = 1 / ((c * r ** 2 + 1))
    fig = plt.figure()
    plt.plot(r, z, 'r', label='f(x)')
    plt.plot(x, y_interpolated, label='p(x)')
    plt.legend()
    plt.plot()
    plt.show()
    r_1 = np.linspace(-1, 1, 100)
    error_est = abs((f(c, r_1) - newtonmethod(x, y, r_1)))
    fig = plt.figure()
    plt.plot(r_1, error_est, 'r')
    plt.show()


plots(4, 18)