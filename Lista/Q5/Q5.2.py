from sympy import *

grau = 6

#os xs e ys, pontos
xk=[-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5]
fk=[3.99, -5.26, 0.54,1.88,-4.29,-2.59, -0.95, -0.15]
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
