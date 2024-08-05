N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

min_diff = float('inf')

for i in range(K+1):
    temp = A[i+(N-K)-1] - A[i]
    min_diff = min(min_diff, temp)

print(min_diff)