'''

Use a regra dos trapézios para aproximar o valor da integral ∫0.4709 −0.32902 e**−x2dx. Use o número n de subintervalos indicado.

'''
import math

exact = 0.755815

a, b = -0.37744, 0.96498
def f(x):
    return math.exp(-x ** 2)

def trapezio(f, h, xs):
    last = len(xs) - 1
    soma = f(xs[0]) + f(xs[last])
    soma += 2 * sum([f(x) for i, x in enumerate(xs) if i not in [0, last]])
    return (h / 2) * soma

for n in range(8):
    h = (b - a) / 2 ** n
    xs = [a + k * h for k in range(2 ** n + 1)]
    aprox = trapezio(f, h, xs)
    print('qtde:', 2 ** n, 'aprox:', aprox, 'erro:', abs(exact - aprox))

'''
qtde: 1 aprox: 0.6793391224139297 erro: 0.07647587758607033
qtde: 2 aprox: 0.7376218252527469 erro: 0.018193174747253127
qtde: 4 aprox: 0.7513162175625371 erro: 0.004498782437462934
qtde: 8 aprox: 0.754693102170944 erro: 0.0011218978290560289
qtde: 16 aprox: 0.7555345022519804 erro: 0.0002804977480196369       
qtde: 32 aprox: 0.7557446774180551 erro: 7.032258194494823e-05       
qtde: 64 aprox: 0.7557972103037626 erro: 1.778969623744686e-05       
qtde: 128 aprox: 0.7558103428439279 erro: 4.6571560721186955e-06 
'''
