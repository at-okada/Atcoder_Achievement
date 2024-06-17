import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))
matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

result = [0] * M
for row in matrix:
    for i in range(M):
        result[i] += row[i]

for l in range(0,M):
    if A[l] > result[l]:
        print("No")
        sys.exit()

print("Yes")