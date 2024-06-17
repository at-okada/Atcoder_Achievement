N, A = map(int, input().split())
T = list(map(int, input().split()))

end = [0]*N
wait = 0

for i in range(N):
    if wait > 0:
        end[i] = T[i]+ A + wait
    else:
        end[i] = T[i]+A

    print(end[i])

    if i < N - 1: 
        #max関数便利
        wait = max(0, end[i] - T[i + 1])