from sympy import *

grau = 10

#os xs e ys, pontos
xk=[-2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
fk=[0.94, -3.08, 5.33, 2.57, 5.94, 4.39, -2.35, 0.17, 5.38, -1.13, -2.63]
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
