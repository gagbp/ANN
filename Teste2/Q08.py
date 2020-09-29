'''

Encontre os coeficientes do polinômio de grau 5 y=a0+a1x+a2x2+a3x3+a4x4+a5x5 que melhor se aproxima da seguinte lista de 50 pontos

[(-1.92, 6.846), (-1.832, 7.814), (-1.752, 8.676), (-1.672, 8.68), (-1.528, 8.585), (-1.472, 8.466), (-1.408, 8.286), (-1.336, 7.615), (-1.304, 7.234), (-1.144, 6.392), (-1.136, 5.975), (-1.112, 6.032), (-0.928, 4.664), (-0.904, 4.522), (-0.896, 4.918), (-0.736, 4.183), (-0.64, 3.784), (-0.456, 3.935), (-0.32, 4.055), (-0.176, 4.725), (-0.152, 4.583), (-0.12, 4.773), (-0.024, 5.096), (0.064, 5.544), (0.136, 5.963), (0.224, 6.226), (0.28, 6.461), (0.424, 6.827), (0.448, 6.785), (0.472, 6.492), (0.504, 6.482), (0.512, 6.757), (0.608, 6.876), (0.696, 6.388), (0.704, 6.673), (0.896, 5.923), (0.96, 5.657), (1.0, 5.389), (1.024, 5.138), (1.184, 4.091), (1.24, 3.772), (1.312, 3.258), (1.328, 2.858), (1.4, 2.436), (1.496, 2.059), (1.68, 1.469), (1.72, 1.758), (1.832, 2.53), (1.976, 4.815), (1.984, 4.788)]

'''
import math
import random as r
import matplotlib.pyplot as plt
import numpy as np

a,b = -2,2
entrada = [(-1.92, 6.846), (-1.832, 7.814), (-1.752, 8.676), (-1.672, 8.68), (-1.528, 8.585), (-1.472, 8.466), (-1.408, 8.286), (-1.336, 7.615), (-1.304, 7.234), (-1.144, 6.392), (-1.136, 5.975), (-1.112, 6.032), (-0.928, 4.664), (-0.904, 4.522), (-0.896, 4.918), (-0.736, 4.183), (-0.64, 3.784), (-0.456, 3.935), (-0.32, 4.055), (-0.176, 4.725), (-0.152, 4.583), (-0.12, 4.773), (-0.024, 5.096), (0.064, 5.544), (0.136, 5.963), (0.224, 6.226), (0.28, 6.461), (0.424, 6.827), (0.448, 6.785), (0.472, 6.492), (0.504, 6.482), (0.512, 6.757), (0.608, 6.876), (0.696, 6.388), (0.704, 6.673), (0.896, 5.923), (0.96, 5.657), (1.0, 5.389), (1.024, 5.138), (1.184, 4.091), (1.24, 3.772), (1.312, 3.258), (1.328, 2.858), (1.4, 2.436), (1.496, 2.059), (1.68, 1.469), (1.72, 1.758), (1.832, 2.53), (1.976, 4.815), (1.984, 4.788)]
n = 50
xs = [x for (x,y) in entrada]
ys = [y for (x,y) in entrada]

def f(x):
    aux = [y for (t,y) in entrada if t == x]
    return aux[0]


num = 6
fs = [f'x**{i}' for i in range(num)]
def simpson(f, a, b, intvals):
    h = (b - a) / intvals
    xs = [x for (x,y) in entrada]
    last = len(xs) - 1
    soma = f(xs[0]) + f(xs[last])
    soma += 2 * sum([f(xs[i]) for i in range(2, last, 2)])
    soma += 4 * sum([f(xs[i]) for i in range(1, last, 2)])
    return (h / 3) * soma

class BestFunc:
    # usa a regra de simpson para resolver as integrais no sistema

    def __init__(self, f, a, b):
        self.f = f
        self.a = a
        self.b = b

    def coeffs(self, functions, intvals=100):
        A = {} # a_ij = int_a^bfi*fjdx
        n = len(functions)
        for i in range(n):
            A[i] = {}
            for j in range(n):
                if i <= j:
                    def f_ij(x):
                        return eval(functions[i]) * eval(functions[j])
                    A[i][j] = simpson(f_ij, a, b, intvals)
                else:
                    A[i][j] = A[j][i]
        A = [[v for _, v in value.items()] for _, value in A.items()]

        B = []
        for i in range(n):
            def func(x):
                return f(x) * eval(functions[i])
            val = simpson(func, a, b, intvals)# int_a^b(f*fi)dx
            B.append(val)
        coeffs = np.linalg.solve(A, B)
        return coeffs

obj = BestFunc(f, a, b)

coeffs = obj.coeffs(fs, 200)

def s(x):
    if x < 0:
        return f' {x}'
    return f' + {abs(x)}'

combina = ''.join([f'{s(ci)}*{fi}' for ci, fi in zip(coeffs, fs)])
def g(x):
    return eval(combina)

print("y = {}".format(combina))

def erro(x):
    return (f(x) - g(x)) ** 2

err = simpson(erro, a, b, 200)



# método dos minimos quadrados geral
def least_squares(pontos, k): # se k == 1, então o resultado é o mesmo de min_q(pontos)
    # vamos obter um sistema (k+1)x(k+1)
    n = len(pontos)
    A = {}
    B = []
    for i in range(k + 1):
        A[i] = {}
        for j in range(k + 1):
            if j >= i:
                A[i][j] = sum(x ** (i + j) for x, _ in pontos)
            else:
                A[i][j] = A[j][i]
    A = [[A[i][j] for j in range(k + 1)] for i in range(k + 1)]
    for i in range(k + 1):
        B.append(sum(y * x ** i for x, y in pontos))
    coefs = np.linalg.solve(A, B)
    return coefs

pontos = list(zip(xs, ys))
c = least_squares(pontos, k=15)
print(c)

def fit_poly(x):
    return sum(c * x ** i for i, c in enumerate(c)) # sum c[j] * x ** j, j=0,1,2,...,k

erro = sum((y - fit_poly(x)) ** 2 for x, y in pontos)
tq = np.arange(a, b, 0.01)



plt.scatter(xs, ys)

h = (b - a) / n
ta = [a + i * h for i in range(n)]

t = np.arange(a, b, 0.01)
gt = [g(x) for x in t]
plt.plot(t, gt, color='blue', label=f'erro = {err}')

plt.plot(tq, fit_poly(t), 'g', label=f"erro = {erro}")

plt.legend()
plt.show()
'''
y =  + 5.2942634601306455*x**0 + 4.116750832939132*x**1 + 0.016993773853412497*x**2 -5.113293203380938*x**3 -0.01583811206619205*x**4 + 1.02681385597036*x**5
[ 5.30906723e+00  4.57417633e+00 -9.12927044e-02 -9.07586805e+00
  3.59467562e-02  1.16133702e+01  1.20757135e-01 -1.27400007e+01
 -1.10475150e-01  8.00447160e+00  3.26653801e-02 -2.73103706e+00
 -4.14923551e-03  4.79648091e-01  2.67075486e-04 -3.39595424e-02]
'''
