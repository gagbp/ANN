# jacobi
print('Jacobi')
E = [[3,2,1,2], [2,7,2,-3], [1,3,5,3]] # matrix estendida do sistema

def test(matrix, vec):
    err = []
    for row in matrix:
        prod = abs(sum([col * vec for col, vec in zip(row[:-1], vec)]) - row[-1])
        err.append(prod)
    return err

n  = 10
itr = {}
chute = [0,0,0]
for i in range(n):
    xn = []
    for j, row in enumerate(E):
        subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
        subs = (row[-1] - subs) / row[j]
        xn.append(subs)
    print(xn,";", test(E, xn))
    chute = xn

# Seidel
print('\nGauss Seidel')

itr = {}
chute = [0,0,0]
for i in range(n):
    xn = []
    for j, row in enumerate(E):
        chute = xn + chute[len(xn):] # this line updates chute
        subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
        subs = (row[-1] - subs) / row[j]
        xn.append(subs)
    print(xn,";", test(E, xn))
    chute = xn
