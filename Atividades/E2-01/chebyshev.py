import numpy as np
from sympy import *

x=var('x')

def T(o):
    if o == 0:
        return 1
    elif o == 1:
        return x
    else:
        return 2*x*T(o-1) - T(o-2)

def U(o):
    if o == 0:
        return 0
    elif o == 1:
        return 2*x
    else:
        return 2*x*U(o-1) - U(o-2)

#for i in range(0,10):
#    print("T{} = {}".format(i,expand(T(i))))

#for i in range(0,9):
#    print("U{} = {}".format(i,expand(U(i))))

print("Digite o grau do polinômio de Chebyshev: ")
a = int(input())
print("T{} = {}".format(a,expand(T(a))))
print("U{} = {}".format(a,expand(U(a))))