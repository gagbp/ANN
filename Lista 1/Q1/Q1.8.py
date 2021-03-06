# 8. f(x) = (x**2)*cos(e**x) - x - 1
import numpy as np
def f(x):
    return (x**2)*np.cos(np.e**x) - x - 1

print('\n\nmétodo da bisseção\n')
a, b = [0, 2]
n = 100 # número de iterações
for i in range(n):
    m = (a + b) / 2
    if f(m) == 0:
        print('A raiz é:', m)
    elif f(a) * f(m) < 0: # teorema de Bolzano
        b = m
    else:
        a = m
    print(i, m, f(m))

print('\n\nmétodo de Newton\n')
# derivada de f
def df(x):
    return 2*x*np.cos(np.e**x) - (np.e**x)*(x**2)*np.sin(np.e**x) - 1

x0 = 2
n = 10
itr = {}
itr[0] = x0
for i in range(1, n):
    itr[i] = x0 - f(x0) / df(x0)
    x0 = itr[i]

for k, v in itr.items():
    print(k, v, abs(v - m))

print('\n\nmétodo das secantes\n')

n = 11
x0, x1 = [1, 2]
itr = {}
itr[0] = x0
itr[1] = x1

a, b = x0, x1
for i in range(n):
    try:
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) # a - f(a) / ((f(b) - f(a))/ (b - a))
    except:
        raise ValueError(f"Divisão por zero para {a}, {b} na iteração {i}")
    itr[i + 2] = xn
    a, b = b, xn

for k, v in itr.items():
    print(k, v, abs(v - m))

print('\n\nmétodo da posição falsa\n')

n = 30
a, b = [1, 2]
for i in range(n):
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if f(xn) == 0:
        print('A raiz é:', xn)
        break
    elif f(a) * f(xn) < 0:
        b = xn
    else:
        a = xn
    print(i, xn, abs(xn - m))