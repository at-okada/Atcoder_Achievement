N, K = map(int, input().strip().split())
A = list(map(int, input().split()))

new_arr = A[-K:] + A[:-K]

print(*new_arr)
