import itertools

N, K = map(int, input().strip().split())
S = input()

permutations = set(itertools.permutations(S))

count = 0

for perm in permutations:
    T = ''.join(perm)
    flag = False

    for i in range(N - K + 1):
        substring = T[i:i+K] 
        if substring == substring[:: -1]:
            flag = True
            break
    
    if not flag:
        count += 1

print(count)
