import matplotlib.pyplot as plt
import numpy as np
# y' = x**2 + y + 1, y(x0) = y0
# possui única solução pelo EXU

x0, y0 = 0,2
c2 = 0.5
h = 0.1 # tamanho do passo
n = 50

def f(x, y):
    return x**2 + y + 1

def solucao(x):
    return 5*np.e**x - x**2 - 2*x -3

def euler(f, x0, y0, h):
    x = {0: x0}
    y = {0: y0}
    for i in range(1, n):
        x[i] = x0 + i * h # <- listando os pontos na partição
        y[i] = y[i - 1] + f(x[i - 1], y[i - 1]) * h # <- fórmula do método
    return x, y

def heun(f, x0, y0, h):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 2) * (m1 + m2) # <- fórmula do método de Heun
    return x, y

def euler_mid(f, x0, y0, h):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + h * m2 # <- fórmula do método de Heun
    return x, y

def ralston(f, x0, y0, h):
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + (h / 3) * (1* m1 + 2 * m2) # <- fórmula do método de Heun
    return x, y

def rk2(f, x0, y0, c2, h):
    #c1 + c2 = 1 --> c1 = 1 - c2, c2>0
    c1 = 1 - c2
    x = {i: x0 + i * h for i in range(n)}
    y = {0: y0}
    for k in range(n - 1):
        m1 = f(x[k], y[k])
        m2 = f(x[k] + h, y[k] + m1 * h)
        y[k + 1] = y[k] + h * (c1 * m1 + c2 * m2) # <- fórmula do método de Heun
    return x, y

xs, ys = euler(f, x0, y0, h)
x = [v for _, v in xs.items()]
y = [v for _, v in ys.items()]

hxs, hys = heun(f, x0, y0, h)
hx = [v for _, v in hxs.items()]
hy = [v for _, v in hys.items()]

exs, eys = euler_mid(f, x0, y0, h)
ex = [v for _, v in exs.items()]
ey = [v for _, v in eys.items()]

rxs, rys = ralston(f, x0, y0, h)
rx = [v for _, v in rxs.items()]
ry = [v for _, v in rys.items()]

r2xs, r2ys = rk2(f, x0, y0, c2, h)
r2x = [v for _, v in r2xs.items()]
r2y = [v for _, v in r2ys.items()]

t = np.linspace(x0, x0 + n * h, 100)

plt.scatter(x, y, label="Euler")
plt.scatter(hx, hy, label="Heun")
plt.scatter(ex, ey, label="Euler ponto medio")
plt.scatter(rx, ry, label="Raulston")
plt.scatter(r2x, r2y, label="Raulston grau 2")
plt.plot(t, solucao(t))
plt.legend()
plt.show()
