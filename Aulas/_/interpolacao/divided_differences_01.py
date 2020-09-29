pontos = [(0.26, 6.279), (0.27, 5.981), (0.44, 5.496), (0.68, 5.537), (1.55, 7.058), (1.66, 6.552), (1.77, 6.406), (1.89, 7.71), (2.26, 6.885), (2.68, 7.473), (2.77, 8.454), (2.79, 7.647), (2.82, 7.224), (3.03, 7.384), (3.04, 7.925), (3.24, 7.556), (3.27, 8.128), (3.59, 8.006), (3.73, 8.613), (3.76, 9.773), (3.83, 9.539), (4.2, 9.895), (4.32, 10.395), (4.51, 8.739), (4.81, 9.968), (5.01, 9.428), (5.31, 10.727), (5.48, 10.258), (5.5, 10.085), (5.65, 10.795), (5.74, 10.57), (6.08, 10.932), (6.36, 11.376), (6.48, 10.544), (6.58, 11.84), (6.66, 12.334), (6.81, 11.477), (7.08, 12.537), (7.1, 11.473), (7.2, 11.093), (7.52, 12.912), (7.59, 11.82), (7.64, 11.46), (7.7, 11.732), (8.62, 13.715), (8.97, 14.27), (9.01, 13.65), (9.04, 13.701), (9.77, 14.38), (9.91, 13.637)]
xs, ys = zip(*pontos)
n = len(pontos)

# auxiliares
def prod(lista):
    p = 1
    for i in lista:
        p *= i
    return p

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

# algoritmo
def tabela(pontos):
    Y = {}
    Y[0] = {k: v for k, v in enumerate(ys)}
    for j in range(1, n):
        Y[j] = {}
        for i in range(n - j):
            Y[j][i] = (Y[j - 1][i + 1] - Y[j - 1][i]) / (xs[j + i] - xs[i])
    return Y

t = tabela(pontos)
a = [v[0] for k, v in t.items()]

def p(x):
    soma = 0
    for k in range(n):
        termo_k = prod([(x - xi) for i, xi in enumerate(xs) if i < k])
        soma += a[k] * termo_k
    return soma

def eq(coefs):
    equation = ""
    for k in range(n):
        termo_k = "*".join([f'(x{sign(-xi)})' for i, xi in enumerate(xs) if i < k])
        if k == 0:
            equation += str(a[k])
        else:
            equation += f'{sign(a[k])}*' + termo_k
    return equation

poly = eq(a)
print(poly)

# Método das diferenças divididas (de Newton)

import matplotlib.pyplot as plt
import numpy as np

def poly_f(x):
    return eval(poly)

a, b = min(xs) - 0.5, max(xs) + 0.5
t = np.arange(a, b, 0.01)
plt.scatter(xs, ys)
plt.plot(t, poly_f(t), color="red", label="polinômio interpolador")
plt.show()
