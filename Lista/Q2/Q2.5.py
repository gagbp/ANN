# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x
import numpy as np
def g(x):
    return np.e**x - 2*x -1

def f(x):
    return np.log(2*x+1)

n = 10
a, b = [2, 3]
x0 = 0.5
for i in range(10):
    xn = g(x0)
    x0 = xn
    print(x0)