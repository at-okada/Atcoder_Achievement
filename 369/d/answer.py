N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

cum_sum = [0] * (2 * N + 1)
for i in range(1, 2 * N + 1):
    cum_sum[i] = cum_sum[i - 1] + A[(i - 1) % N]

count = 0
for i in range(N):
    for j in range(i + 1, i + N):
        distance = cum_sum[j] - cum_sum[i]
        if distance % M == 0:
            count += 1

print(count)