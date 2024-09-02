N = int(input())
S = [input().strip() for _ in range(N)]

M = max(len(s) for s in S)

grid = [["*"] * M for _ in range(N)]

for i in range(N):
    for j in range(len(S[i])):
        grid[i][j] = S[i][j]

rotated_grid = [[""] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        rotated_grid[i][j] = grid[N-j-1][i]

for i in range(M):
    rotated_grid[i] = "".join(rotated_grid[i]).rstrip('*')

for row in rotated_grid:
    print(row)
