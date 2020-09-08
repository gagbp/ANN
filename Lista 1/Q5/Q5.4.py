
from sympy import *

grau = 4

#os xs e ys,   pontos
xk=[-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5]
fk=[-5.6, -4.03, -0.4, -1.12, 1.51, 2.98, -4.59, 0.56, -4.43, -5.53, 2.14, 4.02, 0.85, 1.37, 5.26, 2.79, 5.16, -2.28, -2.9, -0.61, -3.93, 2.04, 5.61, -2.09, 1.55, -0.59, -5.47, -5.5, 2.64, 2.0, 5.1]
#

#as variaveis
x=var('x')
#

#os coeficientes de Lagrange
Lk=[]
#

#P(x)

print("f(x)=")
print(fk)

for i in range(0,len(xk)):
    L = 1.0
    for j in range (0,len(xk)):
        if i!= j:
            # print('x - x{} / x{} - x{}'.format(j, i, j))
            L = L * (x- xk[j])/(xk[i]-xk[j])
    Lk.append(L)
    print("L{} = {}\n".format(i, expand(Lk[i])))

print("\n")
a=x-x
print("P(x) = ")
for i in range (0, len(xk)):
    a = a+expand(Lk[i] * fk[i])
    print("{} + ".format(expand(Lk[i] * fk[i])))

print('\nExpandindo P(x) = ')
print(expand(a))
