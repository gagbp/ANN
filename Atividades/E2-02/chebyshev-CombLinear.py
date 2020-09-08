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

print("Digite o N: ")
a = int(input())
'''
for i in range(0,a+1):
    print("T{} = {}".format(i,T(i)))
    print("c{} = {}\n".format(i,c(i)))
'''
aprox = F(a)

print("f(x) = {}".format(f(x)))
print("F(x) = {}".format(aprox))

p = plot(f(x), aprox, (x, -1, 1), show=False)
p[1].line_color = 'r'

p.show()

