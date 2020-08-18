def Fk(h, k):
    F1h = {1: 1.423425, 1/2: 1.547362, 1/4: 1.553842, 1/8: 1.559343}
    if k == 1:
        return F1h[h]
    k -= 1
    return (pow(2,1*k) * Fk(h/2, k) - Fk(h, k)) / (pow(2,1*k) - 1)

h = 1 #gambiarra
r = Fk(h, 4)
print(r)