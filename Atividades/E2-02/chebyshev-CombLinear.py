import numpy as np
from sympy import *

x=var('x')

def f(x):
    return 1/(1+x**2)

def T(n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return cos(n*acos(x))

def integFTn(n):
    return Integral(((f(x)*T(n))/sqrt(1-x**2)),(x,-1,1)).evalf()

def integTnTn(n):
    return Integral(((T(n)*T(n))/sqrt(1-x**2)),(x,-1,1)).evalf()

def c(k):
    return integFTn(k)/integTnTn(k)

def F(n):
    if n == 0:
        return c(n)*T(n)
    else:
        return c(n)*T(n) + F(n-1)

print("f(x) = {}\n".format(f(x)))

print("Digite N: ")
N = int(input())

Ts = list()
Cs = list()

for i in range(0,N+1):
    Ts.append(T(i))
    Cs.append(c(i))

print("c = {}".format(Cs))
Fs = Cs[0]*Ts[0]
for i in range(1,N+1):
    Fs += Cs[i]*Ts[i]

print("F(x) = {}\n".format(Fs))

p = plot(f(x), Fs, (x, -1, 1), show=False)
p[1].line_color = 'r'
p.show()
