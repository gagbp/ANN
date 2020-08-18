#-------------------------------------------------------------------------------#

# Questao 1 #

#-------------------------------------------------------------------------------#

print ("bissection.py")
#funcao qualquer
def f(x):
    return x ** 5 - 8 * x - 2

#metodo da bisseçao
a, b = [0,2]
n = 50 #numero de interações
for i in range(n):
    m = (a + b)/2
    if f(m) == 0:
        print (m)
    elif f(a) * f(m) < 0: #teorema de Bolzano
        b = m
    else:
        a = m
    print (m, f(m))

#-------------------------------------------------------------------------------#

print ("\n\n\nnewton.py")
#funcao qualquer
def f(x):
  return x ** 5 - 8 * x - 2

#derivada da funcao
def df(x):
  return 5 * x ** 4 - 8

x0 = 2
n = 10 #numero de interações
itr = {}
itr[0] = x0
for i in range(n):
  itr[i] = x0 - f(x0) / df(x0)
  x0 = itr[i]

for k, v in itr.items():
  print(k, v, abs(v - 1.7392201937014509))

#-------------------------------------------------------------------------------#

print ("\n\n\nsecante.py")
#funcao qualquer
def f(x):
  return x ** 5 - 8 * x - 2

n = 11 #numero de interações
x0,x1 = [1,2]
itr = {}
itr[0] = x0
itr[1] = x1

a, b = x0, x1
for i in range(n):
  xn = (f(b) * a - f(a) * b) / (f(b) - f(a)) # (a-f(a))/(f'(a)) // 
  itr[i + 2] = xn
  a, b = b, xn

for k, v in itr.items():
  print(k, v, abs(v - 1.7392201937014509))

#-------------------------------------------------------------------------------#

print ("\n\n\nposicao_falsa.py")
# posição falsa pode ser mais lento que o metodo da bisseção

#funcao qualquer
def f(x):
  return x ** 5 - 8 * x - 2

n = 30 #numero de interações
a, b = 1, 2
print(f(a), f(b))
for i in range(n):
  if(f(a)*f(b)) < 0:
    xn = (f(b) * a - f(a) * b) / (f(b) - f(a)) # (a-f(a))/(f'(a)) // 
    if f(a) * f(xn) < 0:
      b = xn
    else:
      a = xn
    print(i, xn, abs(v - 1.7392201937014509))


#-------------------------------------------------------------------------------#

# Questão 2 #

#-------------------------------------------------------------------------------#

print ("\n\n\nponto_fixo.py")
# seja g:[a,b]->R
# 0. g tem que ser continua
# 1. g(x)\in [a,b] para todo x\in [a,b]
# 2. |g'(x)| < 1 para todo x\in [a,b]

def g(x):
  return (x + 7 / x) / 2

n = 10
a, b = [1, 2]
x0 = 1.1
for i in range(n):
  xn = g(x0)
  if(x0 == xn):
    break
  else:
    x0 = xn
  print(i, x0)

#-------------------------------------------------------------------------------#

# Questão 3 #

#-------------------------------------------------------------------------------#

print ("\n\n\njacobi.py")

A = [[4,1,1,6], [2,5,2,3], [1,2,4,11]] #matriz estendida do sistema
# 4x +  y +  z =  6 --> x = ( 6 -  y -  z) / 4
# 2x + 5y + 2z =  3 --> y = ( 3 - 2x - 2z) / 2
#  x + 2y + 4z = 11 --> z = (11 -  x - 2y) / 4

def test(matrix, vec):
  err = []
  for row in matrix:
    prod = abs(sum([col*vec for col, vec in zip(row[:-1], vec)]) - row[-1])
    err.append(prod)
  return err


n = 50
itr = {}
chute = [0,0,0]
for i in range(n):
  xn = []
  for j, row in enumerate(A):
    coefs = [-el for k, el in enumerate(row[:-1]) if k!=j]
    vec = [c for k, c in enumerate(chute) if k!=j]
    subs = (row[-1] + sum([c*v for c, v in zip(coefs, vec)])) / row[j]
    xn.append(subs)
  print (i, xn, test(A, xn))
  chute = xn



#-------------------------------------------------------------------------------#

print ("\n\n\nseidel.py")

A = [[4,1,1,6], [2,5,2,3], [1,2,4,11]] #matriz estendida do sistema
# 4x +  y +  z =  6 --> x = ( 6 -  y -  z) / 4
# 2x + 5y + 2z =  3 --> y = ( 3 - 2x - 2z) / 2
#  x + 2y + 4z = 11 --> z = (11 -  x - 2y) / 4

def test(matrix, vec):
  err = []
  for row in matrix:
    prod = abs(sum([col*vec for col, vec in zip(row[:-1], vec)]) - row[-1])
    err.append(prod)
  return err


n = 50
itr = {}
chute = [0,0,0]
for i in range(n):
  xn = []
  for j, row in enumerate(A):
    coefs = [-el for k, el in enumerate(row[:-1]) if k!=j]
    chute = xn + chute[len(xn):]
    vec = [c for k, c in enumerate(chute) if k!=j]
    subs = (row[-1] + sum([c*v for c, v in zip(coefs, vec)])) / row[j]
    xn.append(subs)
  print (i, xn, test(A, xn))
  chute = xn

