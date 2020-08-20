#natural cubic spline

print("Encontrar coeficientes natural cube spline eo10")
print("Digite a quantidade de pontos:")
qtdPontos = 5
xs=[-2,-1,0,1,2]
fxs=[0.2,0.5,1,0.5,0.2]

#estamos resolvendo o exercicio passado, portanto existem: 24 coeficientes
As=[0.2,0.5,1,0.5,0.2]
Bs=[]
Cs=[]
Ds=[]

#lendo os pontos e definindo os ai, i = 0..qtdPontos
#print("Digite os valores: x [enter] y [enter]")
#for i in range(0,qtdPontos):
#    xs.append(float(input()))
#    fxs.append(float(input()))
#    As.append(fxs[i])

Hs = []

#definindo os intervalos
for i in range(0, qtdPontos-1):
    Hs.append(xs[i+1] - xs[i])

#definido alfas
alfas=[]
for i in range(1, qtdPontos-1):
    alfas.append(3/Hs[i] * (As[i+1] - As[i]) - 3/Hs[i-1] * (As[i] - As[i-1]))

# print("size alfa {}".format(len(alfas)))
ls = []
mis=[]
zs=[]

#definindo para indice 0
ls.append(1.0)
mis.append(0.0)
zs.append(0.0)

for i in range(1, qtdPontos-1):
    ls.append(2*(xs[i+1] - xs[i-1]) - Hs[i-1]*mis[i-1])
    mis.append(Hs[i]/ls[i])
    zs.append((alfas[i-1] - Hs[i-1]*zs[i-1])/ls[i])

#definindo para indice n
ls.append(1.0)
mis.append(0.0)
zs.append(0.0)

for i in range(0, qtdPontos):
    Cs.append(0.0)
    Bs.append(0.0)
    Ds.append(0.0)

for i in range(0, qtdPontos-1):
    Cs[qtdPontos-2 - i] = zs[qtdPontos-2 - i] - mis[qtdPontos-2 - i]*Cs[qtdPontos-2 - i+1]
    Bs[qtdPontos-2 - i]=(As[qtdPontos-2 - i+1] - As[qtdPontos-2 - i])/Hs[qtdPontos-2 - i] - Hs[qtdPontos-2 - i]*(Cs[qtdPontos-2 - i+1] + 2*Cs[qtdPontos-2 - i])/3
    Ds[qtdPontos-2 - i]=(Cs[qtdPontos-2 - i+1] - Cs[qtdPontos-2 - i])/(3*Hs[qtdPontos-2 - i])

print("Hs")
print(Hs)

print("Alfas")
print(alfas)

print("ls")
print(ls)

print("mis")
print(mis)

print("zs")
print(zs)

for i in range(0,qtdPontos-1):
    print("{}; {}; {}; {}".format(As[i],Bs[i],Cs[i],Ds[i]))
