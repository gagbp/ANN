# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x

def g(x):
    return (x + 7 / x) / 2

def f(x):
    return x**2 - 7

n = 10
a, b = [2, 3]
x0 = 2.64575

for i in range(10):
    xn = g(x0)
    x0 = xn
    print(x0)