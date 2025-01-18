N, D = map(int, input().strip().split())

T = []
L = []

for i in range(N):
    t, l = map(int, input().strip().split())
    T.append(t)
    L.append(l)

for l in range(D):
    G = []
    for r in range(N):
        L[r] = L[r] + 1
        G.append(L[r]*T[r])
        
    print(max(G))