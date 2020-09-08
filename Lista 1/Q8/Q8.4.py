import math
import numpy as np
import sympy as sy

def f(x):
    return np.e**(-x**2)

x0 = 1

def f1(p, h):
    return (f(p) - f(p - h)) / h

def f2(p, h):
    return (f(p + h) - f(p - h)) / (2*h)

def f3(p, h):
    return (f(p - 2*h) - 8*f(p - h) + 8*f(p + h) - f(p + 2*h)) / (12 * h)


hs = [1, .1, .05, .025, .0125]

for h in hs:
    print('aprox:', f3(x0, h))

x0 = 1 # <- deriva neste ponto
n = 30 # <- usa essa quantidade de pontos
der = 10 # <- deriva este tanto de vezes
h = 1 / n # <- comprimento dos subintervalos em xs
xs = [h * (-1 + i*(2/(n-1))) + x0 for i in range(n)]
print(xs)

A = [[x ** i for x in xs] for i in range(n)]
# print(A)

B = []
for i in range(n):
    if i < der:
        B.append(0)
    else:
        B.append(x0 ** (i - der) * math.factorial(i) / math.factorial(i - der))

# print(B)
c = np.linalg.solve(A, B)

def formula(xs, c):
    soma = 0
    for i in range(n):
        soma += c[i] * f(xs[i])
    return soma

der_f_em_x0 = formula(xs, c)
print('aprox:', der_f_em_x0)

x = sy.Symbol('x')
string = 'cos(x**2)'
F = sy.sympify(string)
exact = sy.diff(F, x, der).subs(x, x0)
print('exact:', exact.evalf())

import random
print('aprox:', random.randint(-10**8, 10 ** 8))
