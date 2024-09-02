N, K = map(int, input().strip().split())
A = list(map(int, input().split()))
count = 0
seat = 0
for i in range(0, N):
    if K - seat - A[i] > 0:
        seat += A[i]
    elif K - seat - A[i] == 0:
        count += 1
        seat = 0
    else:
        count += 1
        seat = A[i]

if seat > 0 :
    count += 1

print(count)