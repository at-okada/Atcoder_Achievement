N, T, P= map(int, input().strip().split())
L = list(map(int, input().split()))

turns = 0

while True:
    count = 0
    for i in range(N):
        if L[i] >= T:
            count += 1
    
    if count >= P:
        break

    for i in range(N):
        L[i] += 1

    turns += 1

print(turns)