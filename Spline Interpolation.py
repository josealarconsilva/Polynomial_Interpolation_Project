import numpy as np
import matplotlib.pyplot as plt


def spline(n, t, y, x):
    h = [None]*n
    b = [None]*n
    for i in range(0, n):
        h[i] = t[i+1]-t[i]
        b[i] = 6*(y[i+1]-y[i])/h[i]
    u = [None]*(n+1)
    v = [None]*(n+1)
    u[1] = 2*(h[0] + h[1])
    v[1] = b[1] - b[0]
    for i in range(2, n):
        u[i] = 2*(h[i]+h[i-1]) - (h[i-1]**2)/u[i-1]
        v[i] = b[i] - b[i-1] - (h[i-1]*v[i-1])/u[i-1]
    z = [0]*(n+1)
    z[n] = 0
    for i in range(n-1, 0, -1):
        z[i] = (v[i] - h[i]*z[i+1])/u[i]
    z[0] = 0
    S = [0] * (n)
    for i in range(0, n):
        S[i] = (z[i]/(6*h[i]))*(t[i+1]-x)**3 + (z[i+1]/(6*h[i]))*(x-t[i])**3 + ((y[i+1]/h[i]) - ((z[i+1]*h[i])/6))*(x-t[i])+(y[i]/h[i]-((z[i]*h[i])/6))*(t[i+1]-x)
    for i in range(0, n):
        if x >= t[n]:
            return S[n-1]
            quit()
        elif x >= t[i] and x <= t[i+1]:
            return S[i]
            quit()


def f(c, x):
    return (1 / (c * x ** 2 + 1))

def plots(c, n):
    x = []
    y = []
    for i in range(0, (n+1)):
        x.append((2*i/n) - 1)
        y.append(f(c, x[i]))
    print(x)
    print(y)
    y_interpolated = []

    for i in range(0, (n+1)):
        y_interpolated.append(spline(n, x, y, ((2*i)/n) - 1))

    print(y_interpolated)

    x_coordinates = x
    y_coordinates = y

    error_calc = []



    r = []
    for i in range(0, 101):
        r.append( -1 + i/50)

    print(r)


    error = []

    for i in range(0, 101):
        error.append(spline(n, x, y, r[i]))
    print("This is", error)

    error2 = error[::-1]
    error2.pop(0)

    error_tot = error + error2

    m = np.linspace(-1, 1, 100)
    z = 1 / ((c * m ** 2 + 1))
    fig = plt.figure()
    plt.plot(m, z, 'm', label='f(x)')
    plt.plot(x, y_interpolated, label='p(x)')
    plt.legend()
    plt.plot()
    plt.show()

    errorwf = []
    for i in range(0, 101):
        errorwf.append(abs(f(c, r[i]) - error_tot[i]))
    plt.plot(r, errorwf)
    plt.show()


plots(4, 10)