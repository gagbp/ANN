#funcao qualquer
def f(x):
    return x ** 5 - 8 * x - 2

#metodo da bisseçao
a, b = [0,2]
n = 10 #numero de interações
for i in range(n):
    m = (a + b)/2
    if f(m) == 0:
        print (m)
    elif f(a) * f(m) < 0:
        b = m
    else:
        a = m
    print (m)
